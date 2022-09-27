#!/usr/bin/python3
"""  queries the Reddit API and returns the number of subscribers """
import requests


def top_ten(subreddit):
    """ return the number of suscriber and 0 if it fails """

    data = requests.get("https://www.reddit.com/r/{}/about.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "example"},
                        allow_redirects=False)
    if data.status_code == 400 or data.status_code == 404:
        print("None")
    else:
        data = data.json()
        for child in data.get("data").get("children"):
            print(child.get("data").get("title"))


if __name__ == '__main___':
    top_ten(subreddit)
