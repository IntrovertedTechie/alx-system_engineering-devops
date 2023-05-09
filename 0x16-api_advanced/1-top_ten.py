#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts .
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for post in children[:10]:
                    print(post['data']['title'])
            else:
                print("No posts available for this subreddit")
        else:
            print("No data available for this subreddit")
    else:
        print("None")
