import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='ur_client_id', \
                     client_secret='ur_client_secret', \
                     user_agent='ur_user_agent', \
                     username='ur_username', \
                     password='ur_password')

subreddit = reddit.subreddit('nootropics')

top_subreddit = subreddit.top(limit = 15)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "author" : [],\
                "body" : []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["author"].append(submission.author)
    topics_dict["body"].append(submission.selftext)


topics_data = pd.DataFrame(topics_dict)

topics_data.to_csv('nootropics.csv', index = False)
topics_data.to_excel(r'C:\Users\Nihar Sanda\Desktop\nootropics.xlsx')
