#!/usr/bin/python3
"""queries the Reddit API
and returns a list containing the titles of all hot articles for
a given subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """
        ......
    """

    data = requests.get("https://www.reddit.com/r/"
                        "{}/hot.json?limit=100&after={}"
                        .format(subreddit),
                        headers={"User-Agent": "example"},
                        allow_redirects=False)
    if data.status_code == 404:
        return None
    d = data.json()
    for post in d.get("data").get("children"):
        print(post.get("data").get("title"))
