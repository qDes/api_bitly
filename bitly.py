import argparse
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
    bitlink = json.loads(response.text).get("link")
    return bitlink


def get_clicks(token, bitlink):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks"
    headers = {'Authorization': f"Bearer {token}"}
    payload = {"units": -1}
    response = requests.get(bit_url, headers=headers,
                            params=payload)
    response.raise_for_status()
    link_clicks = json.loads(response.text).get("link_clicks")[0]
    clicks = link_clicks.get("clicks")
    return clicks


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    parser = argparse.ArgumentParser(description="Link shortener")
    parser.add_argument("--link", required=True,
                        help="insert link to short it")
    args = parser.parse_args()
    link = args.link
    if link.startswith('bit.ly'):
        call_func = get_clicks
    else:
        call_func = short_link
    try:
        result = call_func(token, link)
        print(result)
    except requests.exceptions.HTTPError:
        print("Error. Bad url, try another one.")
