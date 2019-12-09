def list_of_tweet(username,numberTweet):
	import tweepy
	import re
	# l'idee est de recuperer un certain nombre de tweet des utilisateurs en gardant le texte uniquement
	# on ne souhaite pas avoir les RT ainsi que les reponses 

	access_token="3239543231-CiRmGhEUaYfSSSlRAortBS22KvffmQ7KzxsIeC4"

	access_token_secret="dNICY8SGaUCkoTiRwFflwFU5lcCB8h4ghTPG3r6Xy7arT"
	consumer_key="L6KBC06aWFGM3AhwWZxmtaXar"
	consumer_secret="bVjl53P1DRNGr9hm4Wa5VjwFSevaL31cmv9V7HEhHykORi6jIm"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	#on se connecte a twitter avec l'api et nos identifiants 
	i=0
	liste_tweet=[]
	#on parcourt les tweet et filtres à la fois les reponses, RT et liens https
	for tweet in tweepy.Cursor(api.user_timeline,id=username,tweet_mode='extended').items():
		
		if i ==numberTweet:
   			break
		if(tweet.full_text[0]!='@' and tweet.full_text[0:2]!='RT'):
			text = re.sub(r'http\S+', '',tweet.full_text)
			liste_tweet.append(text)
			i=i+1
	return liste_tweet


import tweepy
from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer


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
liste_tweet=list_of_tweet("NonsR971",1000)
tokenizer=RegexpTokenizer(r'\w+')
liste_prop_token=[]
#on parcourt les tweets et pour chaque tweet on le scinde en propositions qu'on va ensuite en transformer en liste de mot 
#ces listes de mots qu'on va reunir dans une grande liste pour former notre Word2Vec
for tweet in liste_tweet:
	liste_prop=re.split(r'[.,?!:;-]',tweet)
	for prop in liste_prop:
		liste_prop_token.append(tokenizer.tokenize(prop))





#user = api.get_user('NonsR971')