import os
# import threading
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

website_path = os.getenv('WEBPAGE_PATH')
page = '_pages/chefbot.html'
rasa_port = '5005'
rasa_actions_port = '5056'
ngrok_interface = ['http://127.0.0.1:4040/api/tunnels',
                   'http://127.0.0.1:4041/api/tunnels']


def update_website(path, page, url):
    def change_socketurl(url):
        return f'    socketUrl: "{url}",\n'

    def push_to_github(website_path):
        os.system(f'cd {website_path} && git pull origin master')
        os.system(f'cd {website_path}'
                  '&& git add .'
                  '&& git commit -m "Updated socket for bot"'
                  '; git push origin master')

    page_path = os.path.join(path, page)
    with open(page_path) as f:
        lines = f.readlines()

    new_lines = [
        change_socketurl(url)
        if "socketUrl" in line
        else line
        for line in lines
    ]

    with open(page_path, 'w') as f:
        f.writelines(new_lines)

    push_to_github(path)
    print(f'Updated page with url: {url}')


def start_ngrok(port_to_expose):
    os.system(f'ngrok http {port_to_expose}')


def get_ngrok_url(ngrok_interface):
    try:
        r = requests.get(ngrok_interface[0])
    except Exception:
        r = requests.get(ngrok_interface[1])
    r = r.json()
    public_url = r['tunnels'][0]['public_url']
    assert 'https' in public_url
    return public_url


def main():
    # threading.Thread(target=start_ngrok, args=(rasa_port))
    url = get_ngrok_url(ngrok_interface)
    print(url)
    if url is not None:
        update_website(website_path, page, url)


if __name__ == '__main__':
    main()
