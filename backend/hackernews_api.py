import requests
import json


TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"
SINGLE_ITEM = "https://hacker-news.firebaseio.com/v0/item/{0}.json" # items are identified by a unique ID (integer)
NR_STORIES = 10

def get_10_top_stories():

	""""""""""""""""""""""""""""" 
	Query the HN Firebase API to get the 10 top stories

	Args: none
	Returns: list of story ids

	"""""""""""""""""""""""""""""
	r = requests.get(TOP_STORIES).json() # using the requests built-in JSON decoder

	return r[:NR_STORIES] # items from the beginning through end-1




def get_details(item_id):

	""""""""""""""""""""""""""""" 
	Query the HN Firebase API to get details from an item using its id

	Args: item id
	Returns: JSON containing the story's details

	"""""""""""""""""""""""""""""
	details = {}
	full_url = SINGLE_ITEM.format(item_id) # new style string formatting to use item_id on the URL

	r = requests.get(full_url).json()

	if (r['type'] == 'story'):
		details['title'] = r['title']
		details['by'] = r['by']
		details['url'] = r['url']
		return json.dumps(details)
	else:
		return None

