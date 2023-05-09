#!/usr/bin/python3
"""
Queries the API and returns a list containing the titles of all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list containing the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for post in children:
                    hot_list.append(post['data']['title'])
                after = data.get('after')
                if after:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
            else:
                return None
        else:
            return None
    else:
        return None
