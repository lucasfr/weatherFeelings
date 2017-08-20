import os
import signal
from flask import Flask
from flask import render_template

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def cacule():
    page = '<html><body><h1>'
    page += 'Hello world'
    page += '</h1></body></html>'
    return page

@app.route("/w")
def malhada():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))