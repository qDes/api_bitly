import argparse
import os
import requests
import json

from dotenv import load_dotenv


def shorten_link(bitly_token, url):
    bit_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {'Authorization': f"Bearer {bitly_token}"}
    payload = {"long_url": url}
    response = requests.post(bit_url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = json.loads(response.text).get("link")
    return bitlink


def get_clicks(bitly_token, bitlink):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks"
    headers = {'Authorization': f"Bearer {bitly_token}"}
    payload = {"units": -1}
    response = requests.get(bit_url, headers=headers,
                            params=payload)
    response.raise_for_status()
    try:
        link_clicks = json.loads(response.text).get("link_clicks")[0]
        clicks = link_clicks.get("clicks")
    except IndexError:
        clicks = 0
    return clicks


if __name__ == "__main__":
    load_dotenv()
    bitly_token = os.getenv("BITLY_GENERIC_TOKEN")
    parser = argparse.ArgumentParser(description="Link shortener or clicks counter")
    parser.add_argument("--link", required=True,
                        help="insert link to short it")
    args = parser.parse_args()
    link = args.link
    if link.startswith('bit.ly'):
        call_func = get_clicks
    else:
        call_func = shorten_link
    try:
        result = call_func(bitly_token, link)
        print(result)
    except requests.exceptions.HTTPError:
        print("Error. Bad url, try another one.")
