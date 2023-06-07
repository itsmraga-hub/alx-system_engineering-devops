#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        no of subscribers or 0 if subreddit requested is invalid"""

    headers = {'User-Agent': 'itsmraga'}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        all_titles = response.json().get("data").get("children")
        for title in all_titles:
            t = title.get('data').get('children')
            print(t)
    else:
        print(None)
