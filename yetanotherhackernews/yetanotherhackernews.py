import time
from hashlib import md5
from datetime import datetime
from flask import Flask,render_template,jsonify,json,request


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def showMachineList():
    return render_template('list.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')