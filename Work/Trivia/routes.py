from flask import Flask, url_for
from app import app

@app.route('/')
def hello():
    url = url_for('about');
    link = '<a href="' + url + '">About us!</a>';
    return link;

@app.route('/about')
def about():
    return 'We are the knights who say Ni!!';

@app.route('/question/<title>')
def question(title):
    message = 'you said ' + title;
    return message;