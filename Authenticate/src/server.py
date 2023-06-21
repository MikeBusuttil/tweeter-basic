from os import environ
from requests_oauthlib import OAuth2Session
from flask import Flask, request, jsonify, redirect, session
from log import stderr as log
from keys import code_verifier, secret_key, code_challenge

from sys import path
path.append("../../Tweet")
from file import write

global auth, token
auth = None

app = Flask(__name__)
app.secret_key = secret_key

@app.route('/auth')
def authorize():
    global auth
    
    auth = OAuth2Session(
        environ["TWITTER_CLIENT_ID"],
        redirect_uri=environ['TWITTER_CALLBACK_URI'],
        scope=["tweet.read", "users.read", "tweet.write", "offline.access"]
    )
    redirect_url, state = auth.authorization_url(
        "https://twitter.com/i/oauth2/authorize",
        code_challenge=code_challenge,
        code_challenge_method="S256"
    )
    session["oauth_state"] = state

    return redirect(redirect_url)

@app.route('/callback', methods=['GET'])
def root():
    global auth

    token = auth.fetch_token(
        token_url="https://api.twitter.com/2/oauth2/token",
        client_secret=environ["TWITTER_CLIENT_SECRET"],
        code_verifier=code_verifier,
        code=request.args.get("code")
    )
    write("../../token.json", token)

    return jsonify(["👍"]), 200

# @app.route('/refresh')
# def refresh():
#     global auth, token
#     token = auth.refresh_token(
#         client_id=environ["CLIENT_ID"],
#         client_secret=environ["CLIENT_SECRET"],
#         token_url="https://api.twitter.com/2/oauth2/token",
#         refresh_token=token["refresh_token"],
#     )
#     log('token               :', token)
#     write("token.json", token)

#     return jsonify({"yes": True}), 200
