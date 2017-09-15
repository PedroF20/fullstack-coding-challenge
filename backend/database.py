import os
import datetime
from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client.NewsData

# The database will save individual items
# and the list of id's for the 10 top items


def saved_top_items():

	""""""""""""""""""""""""""""" 
	Gets the previous top items

	Args: none
	Returns: list of story ids

	"""""""""""""""""""""""""""""

	top_items_tmp = db.top_items.find_one()
	if (top_items_tmp is None):
		return []
	else:
		return top_items_tmp['top_items']




def save_top_items(items):

	""""""""""""""""""""""""""""" 
	Updates the top items

	Args: list of story ids

	"""""""""""""""""""""""""""""

	if db.top_items.count() == 0:
		db.top_items.insert_one({'top_items': items})
	else:
		db.top_items.update_one({}, {'$set': {'top_items': items}})