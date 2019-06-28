from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('form.html')
    
@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return '<h1>Welcome, {0}</h1>'.format(username)    

@app.route("/", methods=['POST'])
# def verify_email(email):
#     email = request.form['email']
#     email_error = ''

#     if email is > 0 

#     if len(email) != '':
#         if (re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email)
#             return True
#         return False    

          
# if verify_email(email) == True:
#     return "Success"
# else:
#     email_error = "Not a valid email address"


def valid_info():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username_error=''
    password_error=''
    verify_password_error = ''
    email_error = ''

    if username == '':
        username_error = "This field is required"
    elif " " in username:
        username_error = "This field cannot contain a space" 
        username = ''   
    else:
        if len(username) <3 or len(username) > 20:
            username_error = "This field must be between 3 and 20 characters"
            username = ''    

    if password == '':
        password_error = "This field cannot be blank" 
    elif " " in password:
        password_error = "This field cannot contain a space" 
        password = ''   
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = "Please choose a password between 3 and 20 characters"  
            password = ''         

    if verify_password == '':
        verify_password_error = "This field is required"
        verify_password= ''
    else:
        if password != verify_password:
            verify_password_error = "Passwords do not match"
            verify_password = ''   

    if len(email) < 3 or len(email) > 20 or " " in email or "@" not in email or "." not in email or email != 0:  
        email_error = "Not a valid email address, please try again!"
    else:
        email = email

                 

    if not username_error and not password_error and not verify_password_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))  
    else:
        return render_template('form.html', username_error=username_error, 
        password_error=password_error,
        verify_password_error=verify_password_error,
        username=username,
        password=password,
        verify_password=verify_password)   


app.run()    

# def is_valid(text):
#     if len(text) > 3 or len(text) < 20:
#         return text
#     else:
#         return False

# def is_empty(text):
#     if text == 0:
#         return True
#     else:
#         return False 