from datetime import datetime
from flask import render_template
from app import app
from mongo import *

@app.route('/')
def index():
    return "Hello, world!";

@app.route('/Create')
def Create():
    CreateTriviaQuestions();
    return "Success!";

@app.route('/Questions')
def Questions():
    questionsDoc = GetAllQuestions();
    output = '';
    for question in questionsDoc['questions']:
        output += question['question'] + '<br />';
    return output;
