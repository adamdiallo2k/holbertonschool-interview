#!/usr/bin/python3
import requests


def count_words(subreddit, word_list):
    """
    Query the Reddit API recursively for hot articles in a subreddit and
    print a sorted count of keywords (case-insensitive) found in the titles.
    """
    if not word_list:
        return

    # Map keywords to their frequency (after converting to lowercase).
    key_freq = {}
    for word in word_list:
        word_low = word.lower()
        if word_low in key_freq:
            key_freq[word_low] += 1
        else:
            key_freq[word_low] = 1

    # Counts dictionary for each keyword.
    counts = {word: 0 for word in key_freq}

    def recursive_count(after):
        """
        Recursively fetch pages of hot articles using the 'after' token.
        """
        url = ("https://www.reddit.com/r/{}/hot.json"
               .format(subreddit))
        params = {'limit': 100, 'after': after}
        headers = {
            'User-Agent': 'python:0-count:v1.0 (by /u/yourusername)'
        }
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])
        # Process each post title.
        for child in children:
            title = child.get("data", {}).get("title", "")
            for token in title.split():
                token_lower = token.lower()
                if token_lower in counts:
                    counts[token_lower] += key_freq[token_lower]
        next_after = data.get("after", None)
        if next_after:
            recursive_count(next_after)
        else:
            return

    recursive_count(None)

    # Sort by descending count, then alphabetically (ascending).
    sorted_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0])
    )
    for word, count in sorted_counts:
        if count:
            print("{}: {}".format(word, count))
