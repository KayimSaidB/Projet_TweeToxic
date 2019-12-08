
import tweepy

access_token="3239543231-CiRmGhEUaYfSSSlRAortBS22KvffmQ7KzxsIeC4"

access_token_secret="dNICY8SGaUCkoTiRwFflwFU5lcCB8h4ghTPG3r6Xy7arT"
consumer_key="L6KBC06aWFGM3AhwWZxmtaXar"
consumer_secret="bVjl53P1DRNGr9hm4Wa5VjwFSevaL31cmv9V7HEhHykORi6jIm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
i=0
liste_tweet=[]
for tweet in tweepy.Cursor(api.user_timeline,id='NonsR971').items():
   if i ==100:
   	break 
   if(tweet.text[0]!='@' and tweet.text[0:2]!='RT'):
   	liste_tweet.append(tweet.text)
   	i=i+1



#user = api.get_user('NonsR971')