import requests


def main(url: str):
    return requests.get(url).json()["url"]
