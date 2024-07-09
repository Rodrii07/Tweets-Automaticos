import random
import schedule
import time
from tweets import tweets
from conexion_twitter import client

published_tweets = set()


def tweet():
    if len(published_tweets) == len(tweets):
        print("Todos los tweets publicados.")
        return

    tweet = random.choice(tweets)

    while tweet in published_tweets:
        tweet = random.choice(tweets)

    try:
        client.create_tweet(text=tweet)
        print(f"Tweet publicado: {tweet}")
        published_tweets.add(tweet)
    except Exception as e:
        print(f"Error al publicar el tweet: {e}")


schedule.every(5).seconds.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
