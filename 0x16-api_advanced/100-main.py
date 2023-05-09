#!/usr/bin/python3
"""
100-main
"""
import sys
from typing import List
from collections import defaultdict
from time import sleep
from requests import get


def count_words(subreddit: str, word_list: List[str], after: str = '', res_dict=None) -> dict:
    """Recursive function that queries the Reddit API, parses the title of all hot articles,
    and returns a sorted count of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).

    Args:
        subreddit (str): subreddit to parse
        word_list (List[str]): list of keywords
        after (str): parameter for pagination
        res_dict (dict): dictionary to store the word count

    Returns:
        dict: a sorted count of given keywords
    """
    if res_dict is None:
        res_dict = defaultdict(int)
    if after is None:
        return res_dict
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower().split()
        for word in word_list:
            res_dict[word.lower()] += title.count(word.lower())

    sleep(1)
    after = data.get('data', {}).get('after', None)
    count_words(subreddit, word_list, after, res_dict)

    return dict(sorted(res_dict.items(), key=lambda x: (-x[1], x[0])))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        results = count_words(sys.argv[1], sys.argv[2].split())
        if results:
            for k, v in results.items():
                print(f"{k}: {v}")
