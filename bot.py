import random
import json
import tweepy
from pantun_ai import generate_pantun

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

hadith = load_json("data/hadith.json")
quran = load_json("data/quran.json")

def pick_content():
    choice = random.choices(
        ["pantun", "hadith", "quran"],
        weights=[60, 20, 20]
    )[0]

    if choice == "pantun":
        return generate_pantun()
    elif choice == "hadith":
        return random.choice(hadith)
    else:
        return random.choice(quran)

client = tweepy.Client(
    consumer_key =     os.environ["TW_API_KEY"],
    consumer_secret =  os.environ["TW_API_SECRET"],
    access_token =     os.environ["TW_ACCESS_TOKEN"],
    access_token_secret=os.environ["TW_ACCESS_SECRET"]
)

tweet = pick_content()
client.create_tweet(text=tweet)
print("Tweet posted successfully")
