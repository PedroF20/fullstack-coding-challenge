import time
import threading
import database
from hashlib import md5
from datetime import datetime
from flask import Flask,render_template,jsonify,json,request,Response
from hackernews_api import get_10_top_items, get_details


app = Flask(__name__)
app.config.from_object(__name__)


def get_top_items():

	""""""""""""""""""""""""""""" 
	Gets the current top items and saves them.
	Returns the items as JSON objects

	Args: none
	Returns: JSON containing the story's details

	"""""""""""""""""""""""""""""
	# We have to check for new data every 10 minutes (less for testing purposes)
	# time here is in seconds
	threading.Timer(20, get_top_items).start()

	detailed_list = []

	item_id_list = get_10_top_items()
	database.save_top_items(item_id_list)

	print item_id_list

	for x in item_id_list:
		tmp = get_details(x)
		detailed_list.append(tmp)

	return detailed_list



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.route('/')
def show_items():

	final = []
	tmp = database.saved_top_items()
	
	for i in tmp:
		final.append(get_details(i))
	return jsonify(final)


get_top_items()


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
