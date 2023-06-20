docker build -t test-tweet -f ./test/Dockerfile .
docker run -it --rm --name test-tweet \
  -e TWITTER_CONSUMER_API_KEY=$TWITTER_CONSUMER_API_KEY \
  -e TWITTER_CONSUMER_API_KEY_SECRET=$TWITTER_CONSUMER_API_KEY_SECRET \
  -e TWITTER_ACCESS_TOKEN=$TWITTER_ACCESS_TOKEN \
  -e TWITTER_ACCESS_TOKEN_SECRET=$TWITTER_ACCESS_TOKEN_SECRET \
  -e TWITTER_CLIENT_ID=$TWITTER_CLIENT_ID \
  -e TWITTER_CLIENT_SECRET=$TWITTER_CLIENT_SECRET \
  -e TWITTER_CALLBACK_URI=$TWITTER_CALLBACK_URI \
  -v ./src:/app \
  -v ./test/test.jpg:/app/test.jpg \
  -v ./test/test.py:/app/test.py \
  test-tweet
