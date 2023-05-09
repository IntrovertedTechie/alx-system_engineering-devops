#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else None
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
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
