#!/usr/bin/python3
"""
This module contains a function that recursively queries the Reddit API and
returns a list of all hot article titles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and appends the title of each hot post
    to the hot_list.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after', None)
    
    if not posts:
        return hot_list
    
    hot_list += [post['data']['title'] for post in posts]
    
    if after is None:
        return hot_list
    
    return recurse(subreddit, hot_list, after=after)
