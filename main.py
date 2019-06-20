from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('form.html')
    
@app.route("/hello", methods=['POST'])
def hello():
    name = request.form['username']
    return render_template('hello_greeting.html', name = name)    
   
app.run()    
