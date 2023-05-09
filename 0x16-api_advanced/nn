#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def count_words(subreddit, word_list, word_counts={}):
    """Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords"""
    hot_list = recurse(subreddit, [])
    if hot_list:
        for title in hot_list:
            words = title.lower().split()
            for word in words:
                if word.rstrip('.,?!') in word_list:
                    word_counts[word.rstrip('.,?!')] = word_counts.get(word.rstrip('.,?!'), 0) + 1
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print("{}: {}".format(word, count))
    else:
        print("No posts match or subreddit is invalid.")


def recurse(subreddit, hot_list=[], after="", word_counts={}):
    """Returns a list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
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
                    return recurse(subreddit, hot_list, after, word_counts)
                else:
                    return hot_list
            else:
                return None
        else:
            return None
    else:
        return None
