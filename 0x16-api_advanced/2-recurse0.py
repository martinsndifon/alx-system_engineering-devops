#!/usr/bin/python3
"""Advanced API module using reddit api endpoint"""
import requests


def recurse(subreddit, count=0, after=None, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list of all hot article
    titles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set the parameters to retrieve the next 100 hot articles
    # +(maximum allowed by the Reddit API)
    params = {"limit": 100, "count": count, "after": after}
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()

    # Check if there are no hot articles for the subreddit
    if not data["data"]["children"]:
        if count == 0:
            return None
        else:
            return hot_list

    # Add the titles of the hot articles to the list
    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    # Recursively call the function to retrieve the next 100 hot articles
    return recurse(subreddit, count=count+100, after=data["data"]["after"],
                   hot_list=hot_list)
