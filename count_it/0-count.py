#!/usr/bin/python3
import requests


def count_words(subreddit, word_list):
    """
    Queries the Reddit API recursively for all hot articles in a given subreddit
    and prints a sorted count of given keywords (case-insensitive), based on the
    title text.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
    """
    if not word_list:
        return

    # Create a mapping of lower-case words to their frequency in word_list.
    # This ensures that duplicates (e.g., "java", "JavA") multiply the count.
    key_freq = {}
    for word in word_list:
        word_low = word.lower()
        if word_low in key_freq:
            key_freq[word_low] += 1
        else:
            key_freq[word_low] = 1

    # The counts dictionary will hold the accumulated count of each keyword.
    counts = {word: 0 for word in key_freq}

    def recursive_count(after):
        """
        Helper recursive function to fetch Reddit hot articles page-by-page.
        """
        url = ("https://www.reddit.com/r/{}/hot.json"
               .format(subreddit))
        # Use limit=100 (maximum allowed) and pass the after token.
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
        # Process each post's title.
        for child in children:
            title = child.get("data", {}).get("title", "")
            # Split the title by whitespace. Since we want an exact match,
            # tokens with punctuation (e.g., 'java!') do not count.
            for token in title.split():
                token_lower = token.lower()
                if token_lower in counts:
                    # Each occurrence gets weighted by the keyword frequency.
                    counts[token_lower] += key_freq[token_lower]
        # Get the next page token.
        next_after = data.get("after", None)
        if next_after:
            recursive_count(next_after)
        else:
            return

    # Start the recursive processing from the first page.
    recursive_count(None)

    # Sort results: descending order by count, then ascending alphabetical.
    sorted_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0])
    )
    for word, count in sorted_counts:
        if count:
            print("{}: {}".format(word, count))
