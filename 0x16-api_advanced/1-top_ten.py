#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'My Python Script 1.0 (by /u/generic_username)'}
    url = f'https://reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        # Check if the response is valid JSON
        try:
            data = response.json()
        except ValueError:
            print(None)
            return

        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
        else:
            print(None)

    except requests.HTTPError:
        print(None)
    except requests.RequestException as e:
        print(None)
