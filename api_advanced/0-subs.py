#!/usr/bin/python3
"""Function that returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
          data = response.json()
          return data['data']['subscribers']
    else:
            return 0
    except Exception as e:
    return 0