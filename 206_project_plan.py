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

	def test_infoList_method(self)
		tupleList = [("title", "YO"), ("director","SUP"), ("rating", 99), ("actors", ["ted", "bill"]), ("languages", 1)]
		M = Movie(Dict(tupleList))
		self.assertEqual(M.infoList, ["Y0", "SUP", 99, ["ted", "bill"], 1])

## Remember to invoke all your tests...

if __name__ == "__main__":
	unittest.main(verbosity=2)