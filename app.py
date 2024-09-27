from flask import Flask, render_template, request, redirect, url_for
from routes import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
