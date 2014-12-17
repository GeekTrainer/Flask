from flask import Flask, url_for, request, render_template
from app import app
import redis

r=redis.StrictRedis('localhost',6379,0, decode_responses=True,charset='utf-8');

@app.route('/')
def hello():
    url = url_for('about');
    link = '<a href="' + url + '">About us!</a>';
    return link;

@app.route('/about')
def about():
    return 'We are the knights who say Ni!!';

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        # Redis code to load question
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html',
                               question = question)
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        # Redis code to load answer
        answer=r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html',
                                   answer = answer,
                                   submittedAnswer = submittedAnswer);

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('CreateQuestion.html');
    elif request.method == 'POST':
        question = request.form['question'];
        answer = request.form['answer'];
        title = request.form['title'];

        # Redis code to save question and answer
        r.set(title+':question',question);
        r.set(title+':answer',answer);      

        return render_template('CreatedQuestion.html',
                               question = question);
    return;