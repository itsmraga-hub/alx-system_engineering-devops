#!/usr/bin/python3
""" A recursive function that queries the Reddit API """

import requests
import sys


def recurse(subreddit, hot_list=[], after='', count=0):
    """Returns:
          list containing the titles of all hot articles for the subreddit
          or None if queried subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {'User-Agent': 'itsmraga'}
    r = requests.get(url, headers=headers,
                     params={'after': after, 'limit': 100, 'count': count},
                     allow_redirects=False)

    if r.status_code == 200:
        res = r.json()/get('data')
        after = r.json().get('data').get('after')
        list_titles = r.json().get('data').get('children')

        for title in list_titles:
            hot_list.append(title.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)

        return hot_list
