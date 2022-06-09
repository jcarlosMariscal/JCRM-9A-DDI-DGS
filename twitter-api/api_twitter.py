from sys import displayhook
import tweepy
import credentials as cre
import pandas as pd #Para mejor visualización
import numpy as np


def twitter_setup():
  auth = tweepy.OAuthHandler(cre.API_KEY, cre.API_SECRET_KEY)
  auth.set_access_token(cre.ACCESS_TOKEN, cre.ACCESS_TOKEN_SECRET)

  api = tweepy.API(auth)
  return api

req = twitter_setup()
# public_tweets = req.home_timeline()
# for tweet in public_tweets:
#     print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*3}')

tweets = req.user_timeline(screen_name='Carlos24812802', count=200)
print('Numero de tuits extraidos: {}. \n'.format(len(tweets)))

print("5 recent tweets: \n")
for tweet in tweets[:5]:
  print(tweet.text)
  print('')

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
displayhook(data.head(10))

data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['ID'] = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
displayhook(data.head(10))

# dfTweet = data.head(10).copy()
# displayhook(dfTweet)