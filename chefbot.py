import argparse
import atexit
import subprocess
from dotenv import load_dotenv
import os
import time
import update_website
import shutil

load_dotenv(".env")


def get_var(name):
    var = os.getenv(name)
    if var is None:
        raise RuntimeError(f"Couldn't find environment variable {name}")
    return var


CONFIG_PATH = get_var("BOT_CONFIG")
DOMAIN_PATH = get_var("BOT_DOMAIN")
ENDPOINT_PATH = get_var("BOT_ENDPOINT")
DUCKLING_PATH = get_var("DUCKLING_PATH")
WEB_ADR = get_var("WEB_ADR")
BOT_MODELS = get_var("BOT_MODELS")
BOT_CREDENTIALS = get_var("BOT_CREDENTIALS")
LOG_FILE = get_var("LOG_DIR")

processes = []
log_fhs = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="Run in local shell")
    parser.add_argument("--nlu", action="store_true", help="Run nlu shell only")
    args = parser.parse_args()

    # Clear old logs
    shutil.rmtree(LOG_FILE)
    os.mkdir(LOG_FILE)

    # If nlu run locally
    if args.nlu:
        args.local = True

    print("Running chefbot processes")

    if not args.local:
        start_ngrok()
        time.sleep(2)
        subprocess.run(
            ["python3", "update_website.py"], stderr=subprocess.DEVNULL
        )

    start_duckling()
    if args.nlu:
        start_nlu()
    else:
        start_action_server()
        start_bot(args.local)

    while True:
        try:
            pass
        except KeyboardInterrupt:
            break


def start_p(name, commands, out="file"):
    if out == "shell":
        stdout = None
        stderr = None
    elif out == "file":
        stdout = create_log(name)
        stderr = stdout
        log_fhs.append(stdout)

    p = subprocess.Popen(commands, stdout=stdout, stderr=stderr)
    processes.append(p)


def create_log(name):
    fh = open(f"{LOG_FILE}/{name}.log", "a")
    return fh


def start_ngrok():
    start_p("ngrok", ["ngrok", "http", "5005"], "shell")


def start_duckling():
    start_p("duckling", [DUCKLING_PATH, "-p 8000"])


def start_action_server():
    start_p("rasa_actions", ["rasa", "run", "actions", "--actions", "bot.src.actions"])


def start_bot(local):
    args = [
        "--model",
        BOT_MODELS,
        "--endpoints",
        ENDPOINT_PATH,
    ]

    if local:
        start_p("rasa", ["rasa", "shell"] + args, "shell")
    else:
        start_p(
            "rasa",
            ["rasa", "run", "--enable-api", "--cors", WEB_ADR, "--credentials", BOT_CREDENTIALS]
            + args,
        )


def start_nlu():
    start_p("rasa_nlu", ["rasa", "shell", "nlu", "--model", BOT_MODELS], "shell")


def cleanup():
    for p in processes:
        name = p
        p.terminate()
        print(f"Terminate {name}")
    print("Ended all chefbot processes")
    [i.close() for i in log_fhs]


atexit.register(cleanup)


if __name__ == "__main__":
    main()
