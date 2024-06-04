#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'My Python Script 1.0 (by /u/generic_username)'}

    url = f'https://reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        else:
            print(None)

    except requests.HTTPError:
        print(None)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")