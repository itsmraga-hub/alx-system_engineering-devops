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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json().get("data").get("subscribers")
        return (subscribers)

    return (0)
