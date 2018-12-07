# pip install praw
# https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

import praw  
import json

reddit = praw.Reddit(client_id='meMj6xhRrgZ8qQ',
                        client_secret='qTXcdNEBxf5wfbYcMfOsbsIn8Mc',
                        user_agent='android:com.example.myredditapp:v1.2.3 (by /u/davidiwu)')

print(reddit.read_only)

# posts = json.dumps({})

for submission in reddit.subreddit('askreddit').hot(limit=100):
    print(submission.title)