from os import environ, path
from requests_oauthlib import OAuth2Session
from flask import Flask, request, jsonify, redirect, session
from .log import stderr as log
from .keys import code_verifier, secret_key, code_challenge

repo_root = path.realpath(__file__).rsplit('/', 3)[0]
from sys import path
path.append(f"{repo_root}/Tweet")
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
    write(f"{repo_root}/token.json", token)

    return jsonify(["👍"]), 200

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=80, debug=True)
