#!/usr/bin/python3
"""queries the Reddit API
and returns a list containing the titles of all hot articles for
a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        return the list of all hot articles
    """

    data = requests.get("https://www.reddit.com/r/{}/hot.json"
                        .format(subreddit),
                        headers={"User-Agent": "example"},
                        params={"after": after},
                        allow_redirects=False)
    if data.status_code != 200:
        return None
    for i in data.json().get("data").get("children"):
        hot_list.append(i.get("data").get("title"))
    after = data.json().get("data").get("after")
    if after is not None:
        recurse(subreddit, hot_list, after=after)
    return(hot_list)
