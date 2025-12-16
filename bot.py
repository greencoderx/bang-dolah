import os
import json
import random
from datetime import datetime
import tweepy
from pantun_ai import generate_pantun, translate_to_english

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

quran = load_json("data/quran.json")

client = tweepy.Client(
    consumer_key=os.environ["TW_API_KEY"],
    consumer_secret=os.environ["TW_API_SECRET"],
    access_token=os.environ["TW_ACCESS_TOKEN"],
    access_token_secret=os.environ["TW_ACCESS_SECRET"]
)

def is_friday():
    return datetime.utcnow().weekday() == 4

if is_friday():
    tweet = random.choice(quran)
    client.create_tweet(text=tweet)
    print("Friday Qur’an tweet posted")
else:
    pantun = generate_pantun()
    translation = translate_to_english(pantun)

    tweet1 = client.create_tweet(text=pantun)
    client.create_tweet(
        text="English translation:\n" + translation,
        in_reply_to_tweet_id=tweet1.data["id"]
    )
    print("Pantun thread posted")
