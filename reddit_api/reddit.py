import praw
from praw.exceptions import RedditAPIException
from prawcore import ResponseException, OAuthException, NotFound

SUBREDDIT = "learnprogramming"

try:
    # Create a Reddit instance using your credentials to access its API
    reddit = praw.Reddit(client_id = "client_id",
                         client_secret = "client_secret",
                         username = "reddit_username",
                         password = "reddit_password",
                         user_agent="User Agent Test",
                         ratelimit_seconds=100,
                         )
    # Get subreddit latest posts
    for submission in reddit.subreddit(SUBREDDIT).new(limit=5):
        print(f"Title: {submission.title}")
        print(f"\tAuthor: {submission.author}")
        print(f"\tScore: {submission.score}")

# Exceptions handling for bad credentials / authentication / server error
# Client Exception handling can be added as well
except (ResponseException, NotFound) as re:
    print("Your credential are wrong or the subreddit does not exist")
    print(repr(re))

except OAuthException as oae:
    print("Your username or password are incorrect")
    print(repr(oae))

except RedditAPIException as rapie:
    print("Server Side Error")
    print(repr(rapie))
    print(RedditAPIException.error_type)

