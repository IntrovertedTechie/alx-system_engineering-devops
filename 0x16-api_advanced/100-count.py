#!/usr/bin/env python3
"""
Queries the Reddit API and counts the occurrences of each keyword.
"""

import requests


def recurse(subreddit, word_list, count_dict={}, after=None):
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
                    title = post['data']['title'].lower()
                    for word in word_list:
                        if word.lower() in title and not any(c.isalpha() for c in title[title.index(word.lower()) - 1]):
                            count_dict[word.lower()] = count_dict.get(
                                word.lower(), 0) + title.count(word.lower())
                after = data.get('after')
                if after:
                    return recurse(subreddit, word_list, count_dict, after)
                else:
                    sorted_counts = sorted(
                        count_dict.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        print("{}: {}".format(word, count))
            else:
                return None
        else:
            return None
    else:
        return None
