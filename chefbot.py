import argparse
import atexit
import subprocess
from dotenv import load_dotenv
import os
import time

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

processes = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true")
    args = parser.parse_args()

    print("Starting Chefbot processes")

    if not args.local:
        start_ngrok()
        time.sleep(2)

    start_duckling()
    start_action_server()
    start_bot(True)

    while True:
        pass


def start_p(commands):
    p = subprocess.Popen(commands)
    processes.append(p)


def start_ngrok():
    start_p(["ngrok", "http", "5005"])


def start_duckling():
    start_p([DUCKLING_PATH, "-p 8000"])


def start_action_server():
    start_p(["rasa", "run", "actions", "--actions", "bot.src.actions"])


def start_bot(local):
    args = [
        "--model",
        "bot/models",
        "--endpoints",
        ENDPOINT_PATH,
    ]

    if local:
        start_p(["rasa", "shell"] + args)
    else:
        start_p(["rasa", "run", "--enable-api", "--cors"] + args)


def cleanup():
    for p in processes:
        name = p
        p.kill()
        print(f"killed {name}")


atexit.register(cleanup)


if __name__ == "__main__":
    main()
