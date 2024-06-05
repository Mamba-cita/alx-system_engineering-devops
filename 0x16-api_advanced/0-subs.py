#!/usr/bin/python3
"""This module queries the Reddit API and returns the number of subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python/requests"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        
        data = response.json()
        return data['data'].get('subscribers', 0)
        
    except requests.RequestException:
        return 0
