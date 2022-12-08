# Importing modules & libraries
import tweepy
import sqlite3
from sqlalchemy import create_engine
import pandas as pd
import json
from datetime import datetime


# We are wrapping all our code into a function
def create_twitter_etl():


    # Access keys & tokens generated when creating our Twitter developer account
    access_key = 'KXCJ1QMGyG7ANRlhC1OIDgRz4'
    access_secret = 'cD54CatwAVXSKjXQDzLVZbzZmwlYeSHsBxgNMM7JpdYYDnaES5'
    consumer_key = '3239110994-4MXy7CK8ksrtMIqi7yPBNCvC4hneEBRW1j75Rpb'
    consumer_secret = 'uWfLcCMOZG7lAuqSlNyaFkabrBhkpNLSKpZcYmGzLbHE4'


    # Creating a conn between our script to Twitter api
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)


    # Extract of ETL
    # Creating an API object
    api = tweepy.API(auth)

    # We are selecting the user's name, last 100 tweets and the tweet mode is extended
    tweets = api.user_timeline(screen_name='@BillyM2k',
                            count = 100,
                            include_rts = False,
                            tweet_mode = 'extended'
                            )
    

    # Looping through all the tweets
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]
        

        # Transform of ETL
        # Here we are selecting a specific set of data we want
        cleaned_tweet = {"user": tweet.user.screen_name,
                        "text": text,
                        "favorite_count": tweet.favorite_count,
                        "retweet_count": tweet.retweet_count,
                        "created_at": tweet.created_at}
        

        # Appending the data into a list we created above
        tweet_list.append(cleaned_tweet)
    

    # Converting our data to a pandas dataframe
    df = pd.DataFrame(tweet_list)
    df.to_csv('shibetoshi_nakamoto_data.csv')

    
    # Load of ETL
    # We are creating a connection to SQlite using SQL Alchemy
    engine = create_engine('sqlite:///tweet_details.db', echo=True)
    sqlite_connection = engine.connect()


    # Naming our table and importing the dataframe to our table
    sqlite_table = "TwitterData"
    df.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=False)


    # Closing our connection
    sqlite_connection.close()



# Calling our function here
create_twitter_etl()