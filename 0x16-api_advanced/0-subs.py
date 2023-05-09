#!/usr/bin/python3
"""Advanced API module using reddit api endpoint"""
import requests

def number_of_subscribers(subreddit):
    """Request reddit api and return subreddit count"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    subscribers = 0
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        subscribers = data["data"]["children"][1]["data"]["subreddit_subscribers"]
        return subscribers
    except requests.exceptions.HTTPError as error:
        return subscribers

