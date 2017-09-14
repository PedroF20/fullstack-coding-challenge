import requests


TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
SINGLE_ITEM = "https://hacker-news.firebaseio.com/v0/item/%d.json" # items are identified by a unique ID (integer)
NR_STORIES = 10

def get_10_top_stories():

	""""""""""""""""""""""""""""" 
	Query the HN Firebase API to get the 10 top stories

	Args: none
	Returns: list of story ids

	"""""""""""""""""""""""""""""
	r = requests.get(TOP_STORIES).json() # using the requests built-in JSON decoder
	print r[:NR_STORIES]

	return r[:NR_STORIES] # items from the beginning through end-1


get_10_top_stories()