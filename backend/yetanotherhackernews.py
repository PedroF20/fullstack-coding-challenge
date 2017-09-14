import time
from hashlib import md5
from datetime import datetime
from flask import Flask,render_template,jsonify,json,request,Response
from hackernews_api import get_10_top_stories, get_details


app = Flask(__name__)
app.config.from_object(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.route('/')
def show_stories():
	
	final = []
	top_10 = get_10_top_stories()

	for story_id in top_10:
		final.append(get_details(story_id))
	return jsonify(final)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')