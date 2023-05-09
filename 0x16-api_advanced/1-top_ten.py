#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API.
"""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("None")
        return
    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'])




