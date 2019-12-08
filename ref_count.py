import os
import requests
import json

from dotenv import load_dotenv


def short_link(token, url):
    bit_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {'Authorization': f"Bearer {token}"}
    payload = {"long_url": url}
    response = requests.post(bit_url, headers=headers, json=payload)
    response.raise_for_status()
    shortened_link = json.loads(response.text).get("link")
    if shortened_link:
        return shortened_link
    return None


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    print(short_link(token, "https://dvmn.org/modules/"))
