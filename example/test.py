from os import environ, path
repo_root = path.realpath(__file__).rsplit('/', 2)[0]
from sys import path
path.append(f'{repo_root}/Tweet')
from Tweet import Tweet

tweet = Tweet(
    client_id=environ["TWITTER_CLIENT_ID"],
    client_secret=environ["TWITTER_CLIENT_SECRET"],
    callback_uri=environ["TWITTER_CALLBACK_URI"]
)

response = tweet.tweet(
    text="Hello world!",
    image_path=f"{repo_root}/example/test.jpg"
)
print(response[0], response[1])
