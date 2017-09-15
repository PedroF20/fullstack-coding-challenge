import requests
import json


TOP_ITEMS = "https://hacker-news.firebaseio.com/v0/topstories.json"
SINGLE_ITEM = "https://hacker-news.firebaseio.com/v0/item/{0}.json" # items are identified by a unique ID (integer)
NR_ITEMS = 10

def get_10_top_items():

	""""""""""""""""""""""""""""" 
	Query the HN Firebase API to get the 10 top items

	Args: none
	Returns: list of story ids

	"""""""""""""""""""""""""""""
	r = requests.get(TOP_ITEMS).json() # using the requests built-in JSON decoder

	return r[:NR_ITEMS] # items from the beginning through end-1




def get_details(item_id):

	""""""""""""""""""""""""""""" 
	Query the HN Firebase API to get details from an item using its id

	Args: item id
	Returns: JSON containing the story's details

	"""""""""""""""""""""""""""""
	full_url = SINGLE_ITEM.format(item_id) # new style string formatting to use item_id on the URL

	r = requests.get(full_url).json()

	if (r['type'] == 'story'):
		if ('url' in r):
			details = {
				'title': r['title'],
				'by': r['by'],
				'url': r['url'],
			}
			return details
		else:
			details = {
				'title': r['title'],
				'by': r['by'],
				'url': "No URL available",
			}
			return details
	else:
		return None

