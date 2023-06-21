# Tweeter Basic

A simple interface for sending tweets (with optional images) using the Twitter v2 API

## Quick Start

Send a test tweet with the following steps:

- set the following environment variables:
  - TWITTER_CONSUMER_API_KEY
  - TWITTER_CONSUMER_API_KEY_SECRET
  - TWITTER_ACCESS_TOKEN
  - TWITTER_ACCESS_TOKEN_SECRET
  - TWITTER_CLIENT_ID
  - TWITTER_CLIENT_SECRET
  - TWITTER_CALLBACK_URI
- copy `token.json` to the root directory of this repo
- build & run by executing `test/test.sh`

## Prerequisites

- Docker engine
- Twitter project with: 
  - v1.1 API read & write access
  - v2 API access
- a valid OAuth v2 token saved to `token.json`

## 2do

- integrate `token.json` generating code
  - that should probably live in a different directory (ie. Authorize)
  - save token to the root
  - move `file.py` to be a shared library
- create PyPI entry
- improve tests:
  - allow them to run by default without moving all files to same directory
    - remove the test gitignore entries

### future

- add geolocation to tweets:
  - try posting with the v1 API instead of v2:
    - https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update
    - using this format: https://en.wikipedia.org/wiki/GeoJSON
  - wait for an answer to https://stackoverflow.com/questions/75817366/how-to-post-a-tweet-with-geo-data-using-twitter-api-v2-0
    - update forums when answer is found:
      - https://twittercommunity.com/t/how-tweet-with-latitude-longitude-information/189749

### related projects

- https://twitter.com/detroitships
- https://github.com/ezod/aistweet
- [testing grounds](https://twitter.com/HyperB0t)

### resources used

- helpful tutorials:
  - https://developer.twitter.com/en/docs/tutorials/creating-a-twitter-bot-with-python--oauth-2-0--and-v2-of-the-twi
  - https://dev.to/twitterdev/handling-refresh-tokens-in-the-oauth-20-authorization-code-flow-with-pkce-with-flask-481p
- [Twitter POST /2/tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets)
- [Twitter POST /1.1/media/uploads.json](https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload)
  - [v2 uploading future](https://trello.com/c/Zr9zDrJx/109-replacement-of-media-uploads-functionality)
- [media-upload.py](https://gist.github.com/jcipriano/133e44156837360197ba17e7113ddfbc)
