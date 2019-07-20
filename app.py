import os
import sys
import logging

from flask import Flask, session, redirect, make_response, url_for, request, jsonify, render_template

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    # app.run(debug = True)
    app.run(host = '0.0.0.0', debug = True, port = port)