import time
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def showMachineList():
    return render_template('list.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')