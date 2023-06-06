#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        print titles of the first 10 hot posts listed
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    r = requests.get(url, params={"limit": 10}, allow_redirects=False)
    print(r.status_code)
    if r.status_code == 200:
        res = r.json()
        titles = res.get("data")
        for r_title in titles.get("children"):
            print(r_title.get("data").get("title"))
        return
    else:
        print('None')
        return
