#!/usr/bin/python3
"""Advanced API module using reddit api endpoint"""
import requests


def top_ten(subreddit):
    """Request reddit api and return first 10 subreddit titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except requests.exceptions.HTTPError as error:
        print("None")
