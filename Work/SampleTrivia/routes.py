from datetime import datetime
from flask import render_template, request
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
    questions = GetQuestions();
    output = '';
    for question in questions:
        output += question['text'] + '<br />';
    return output;

@app.route('/Question/<int:questionID>', methods=['GET', 'POST'])
def Question(questionID):
    question = GetQuestion(questionID);
    
    if request.method == 'GET':
        return render_template('ask.html',
                         question=question);
    elif request.method == 'POST':
        submittedAnswer = request.form['answer'];
        correctAnswer = question['answer'];
        correct = submittedAnswer == correctAnswer;
        return render_template('answer.html',
                               question = question,
                               correct = correct,
                               submittedAnswer = submittedAnswer);