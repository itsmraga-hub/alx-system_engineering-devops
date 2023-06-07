#!/usr/bin/python3
"""a function that queries the Reddit API returning number of subs"""

import requests


def number_of_subscribers(subreddit):
    """
        number of subscribers function definition
    """
    url = 'https://www.reddit.com/r/'
    if subreddit:
        headers = {'User-Agent': 'itsmraga'}
        r = requests.get(f'{url}{subreddit}/about.json', headers=headers,
                         allow_redirects=False)
        res = r.json()
        if r.status_code == 200:
            subscribers = res.get("data", {}).get("subscribers", 0)
            return subscribers

    return (0)
