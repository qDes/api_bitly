import os
import requests

from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TOKEN")
    url = 'https://api-ssl.bitly.com/v4/user'
    headers = {'Authorization': f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(response.text)
