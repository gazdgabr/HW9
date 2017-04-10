## Your name: Gabriella Gazdecki
## The option you've chosen: Option 2 - API Mashup: Twitter & OMDB

# Put import statements you expect to need here!

import json
import requests
import re
import tweepy
import twitter_info
import collections 
import sqlite3
import unittest
import itertools
import random

## Tweepy setup code borrowed from code given by Professor Cohen this semester.
##### TWEEPY SETUP CODE:

consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

##### END TWEEPY SETUP CODE

## Caching pattern:

cache_filename = "206_final_project_cache.json"

try:
	cache_file = open(cache_filename,'r')
	cache_stuff = cache_file.read()
	cache_file.close()
	cache_dictionary = json.loads(cache_stuff)

except:
	cache_dictionary = {}





## Define class Movie
class Movie():

	def _init_(self):
		return

	def _str_(self):
		return


######## REST OF CODE HERE #########


# Write your test cases here.

class MovieTests(unittest.TestCase):

	def test_constructor_movie(self):
		tupleList = [("title", "YO"), ("director","SUP"), ("rating", 99), ("actors", ["ted", "bill"]), ("languages", 1)]
		M = Movie(Dict(tupleList))
		self.assertNotEqual(type(M), type())

	def test_string_method(self):
		tupleList = [("title", "YO"), ("director","SUP"), ("rating", 99), ("actors", ["ted", "bill"]), ("languages", 1)]
		M = Movie(Dict(tupleList))
		self.assertEqual(M._str_(), type("meow"))

	def test_infoList_method(self):
		tupleList = [("title", "YO"), ("director","SUP"), ("rating", 99), ("actors", ["ted", "bill"]), ("languages", 1)]
		M = Movie(Dict(tupleList))
		self.assertEqual(M.infoList, ["Y0", "SUP", 99, ["ted", "bill"], 1])

	def test_infoList_returntype(self):
		tupleList = [("title", "YO"), ("director","SUP"), ("rating", 99), ("actors", ["ted", "bill"]), ("languages", 1)]
		M = Movie(Dict(tupleList))
		self.assertEqual(type(M.infoList), type(["meow", "meow"]))

class MovieMakingTests(unittest.TestCase):

	def test_makeMovies_length(self):
		A = ["title", "director", "rating", "actors", "languages"]
		B = ["B", "B", 1, [], 1]
		C = ["C", "C", 1, [], 1]
		D = ["D", "D", 1, [], 1]
		dictList = [dict(zip(A,B)), dict(zip(A, C)), dict(zip(A,D))]
		MovieList = makeMovies(dictList)
		self.assertEqual(len(MovieList), 3)

	def test_makeMovies_type(self):
		A = ["title", "director", "rating", "actors", "languages"]
		B = ["B", "B", 1, [], 1]
		C = ["C", "C", 1, [], 1]
		D = ["D", "D", 1, [], 1]
		dictList = [dict(zip(A,B)), dict(zip(A, C)), dict(zip(A,D))]
		MovieList = makeMovies(dictList)
		self.assertEqual(type(MovieList[0]), type(Movie()))

class DatabaseTests(unittest.TestCase):

	def test_db_tweets(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Tweets');
		dis = cur.fetchall()
		conn.close()
		self.assertTrue(len(dis)>=3)

	def test_db_movies(self):
		conn = sqlite3.connect('final_project_tweets.db')
		cur = conn.cursor()
		cur.execute('SELECT * FROM Movies');
		dat = cur.fetchall()
		conn.close()
		self.assertTrue(len(dat)>=3)	
		

## Remember to invoke all your tests...

if __name__ == "__main__":
	unittest.main(verbosity=2)