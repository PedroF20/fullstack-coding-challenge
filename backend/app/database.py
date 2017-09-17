import os
import datetime
from flask import Flask,render_template,jsonify,json
from pymongo import MongoClient
from hackernews_api import get_10_top_items, get_details


client = MongoClient('localhost:27017')
db = client.NewsData

# The database will save individual items
# and the list of id's for the 10 top items
# and translations


def saved_top_items():

	""""""""""""""""""""""""""""" 
	Gets the previous top items

	Args: none
	Returns: list of item ids

	"""""""""""""""""""""""""""""

	top_items_tmp = db.top_items.find_one()
	if (top_items_tmp is None):
		return []
	else:
		return top_items_tmp['top_items']



def save_top_items(items):

	""""""""""""""""""""""""""""" 
	Updates the top items

	Args: list of item ids

	"""""""""""""""""""""""""""""

	if (db.top_items.count() == 0):
		db.top_items.insert_one({'top_items': items})
	else:
		db.top_items.update_one({}, {'$set': {'top_items': items}})



def find_item(item_id):

	""""""""""""""""""""""""""""" 
	Finds an item

	Args: item id
	Returns: JSON object of the item

	"""""""""""""""""""""""""""""
	r = db.items.find_one({'item_id': item_id})
	if r is None:
		return None
	else:
		return get_details(r)


def save_item(item_id):
    
	""""""""""""""""""""""""""""" 
	Saves an item

	Args: item id

	"""""""""""""""""""""""""""""
	r = db.items.find_one({'item_id': item_id})

	if r is None:
		db.items.insert_one(jsonify(r))



def update_item(item_id):

	""""""""""""""""""""""""""""" 
	Updates an item

	Args: item id

	"""""""""""""""""""""""""""""

	r = db.items.find_one({'item_id': item_id})
	db.stories.update_one({'item_id': item_id}, {'$set': jsonify(r)})



