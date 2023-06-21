docker build -t twitter-auth -f ./Authenticate/Dockerfile .
docker run -it --rm --name twitter-auth \
  -e TWITTER_CLIENT_ID=$TWITTER_CLIENT_ID \
  -e TWITTER_CALLBACK_URI=$TWITTER_CALLBACK_URI \
  -e TWITTER_CLIENT_SECRET=$TWITTER_CLIENT_SECRET \
  -v ./:/app \
  -p 80:80 \
  twitter-auth
