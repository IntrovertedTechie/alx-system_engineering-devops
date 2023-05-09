#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after='', counter={}):
    """Prints a sorted count of given keywords."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1

    after = data.get('data', {}).get('after', '')
    if after is None:
        sorted_words = sorted(counter.items(),
                              key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, after, counter)
