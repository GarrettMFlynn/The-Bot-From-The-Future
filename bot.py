import tweepy 
import datetime 
import csv
import random

consumer_key = '4Tf1szRzVZfGEtr4tkd89MyJs' 
consumer_secret = '47tEK6u55bWxemiHy8KheTlEdy4r0h1C1CzQufUJ8thaQXPNTr' 
access_token = '1311400846844928004-MNksawskE1h1ba7NddBbfs4xdan8rP' 
access_token_secret = 'Nvkbd5kbLFriNx3r5eTAn1uvebJNyGl3y3QxxGRPSZPvW' 
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAG7LIAEAAAAAgGbtYfXgcT0MyhR7H6C8PuafPOQ%3DlKMH2HvCeAH8J8o9CjJp2EOGQ8wSWOHPWBOH60ywVRgtITKXd0'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

num_rows = 34
choices = []
sayings = ['In a ', "future, there is a(n) ", "related to ", ". What is it?"]
def publictweet():
    with open('https://raw.githubusercontent.com/GarrettMFlynn/The-Bot-From-The-Future/master/cards.csv') as f:
        reader = csv.reader(f)
        csv_ = list(reader)
        for col in range(3):
            chosen_row = random.choice(range(num_rows))
            choices.append(csv_[chosen_row][col])
    tweettopublish = 'In a ' + choices[0].lower() + " future, there is " + choices[1].lower() + " related to " + choices[2].lower() + ". What is it?"
    print(tweettopublish)
    api.update_status(tweettopublish)

publictweet()


