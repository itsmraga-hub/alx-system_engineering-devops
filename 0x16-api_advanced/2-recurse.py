#!/usr/bin/python3
""" A recursive function that queries the Reddit API """

import requests
import sys


def recurse(subreddit, hot_list=[], after=''):
    """Returns:
          list containing the titles of all hot articles for the subreddit
          or None if queried subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {'User-Agent': 'itsmraga'}
    r = requests.get(url, headers=headers, params={'after': after},
                     allow_redirects=False)

    if r.status_code == 200:
        next_ = r.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = r.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
