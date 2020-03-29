# Reddit_Scraping
This is my first step towards scraping data directly from the reddit. Here i used the python's module PRAW which is a very good module in order to scrape data from reddit. I have scapred the top 20 of all time posts for a particular subreddit. and in that i have scraped the title, score, url, no. of comments, body , date of creation, author of the post. And the id no. of the author who created it. 

In the below code, for al these client_ide, client_secret, user_agent, username, password is of your own reddit account. for the client_is, client_secret, user_agent you have to first be a member of OAuth client. you can check out on the net to create one.

reddit = praw.Reddit(client_id='ur_client_id', \
                     client_secret='ur_client_secret', \
                     user_agent='ur_user_agent', \
                     username='ur_username', \
                     password='ur_password')
