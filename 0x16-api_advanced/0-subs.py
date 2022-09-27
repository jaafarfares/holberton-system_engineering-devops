#!/usr/bin/python3
"""  queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ return the number of suscriber and 0 if it fails """

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "example"},
                        allow_redirects=False)
    if data.status_code == 400 or data.status_code == 404:
        return 0
    data = data.json()
    return data["data"]["subscribers"]

if __name__ == '__main___':
    number_of_subscribers(subreedit)
