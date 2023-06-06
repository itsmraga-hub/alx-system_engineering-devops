#!/usr/bin/python3
"""
    Write a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
        number of subscribers function definition
    """
    url = 'https://www.reddit.com/r/'
    if subreddit:
        r = requests.get(f'{url}{subreddit}/about.json')
        res = r.json()
        if res.get('error') == 404:
            return 0
        subscribers = res.get("data", {}).get("subscribers", 0)
        return subscribers
