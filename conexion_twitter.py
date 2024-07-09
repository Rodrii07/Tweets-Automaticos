import tweepy

api_key = "API_KEY"
api_key_secret = "API_SECRET_KEY"
bearer_token = "BEARER_TOKEN"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_SECRET_TOKEN"

auth = tweepy.OAuth1UserHandler(
    api_key, api_key_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

client = tweepy.Client(
    bearer_token, api_key, api_key_secret, access_token, access_token_secret
)
