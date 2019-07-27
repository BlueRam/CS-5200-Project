# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:27:03 2019

@author: noahd
"""

from flask import Flask, render_template, request,abort,session
from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy import update
import pymysql
import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
import re

 


#Obtain a Connection Object representing an actively checked out DBAPI 
#connection resource 
conn=pymysql.connect(host='localhost',
                     user = 'root',
                     password = 'abcDEFhij123!@')
cursor=conn.cursor()
cursor.execute('USE coffee_database')
engine = create_engine(
        "mysql+pymysql://root:abcDEFhij123!@@localhost/coffee_database", 
        echo = True
        )

PRODUCTS=pd.read_sql('select coffee_id,title,roast,price,description  from coffee_products', "mysql+pymysql://root:abcDEFhij123!@@localhost/coffee_database")
PRODUCTS=PRODUCTS.to_dict('index')


app = Flask(__name__)
app.secret_key="twopac"
@app.route('/')
@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes

            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[2]
           
                
            # Redirect to home page
            return ('Logged in successfully!')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return (render_template('index.html', msg=msg))

@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        total_name=request.form['totalname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        address= request.form['address']
        drinkfreq=request.form['drinkfreq']
        roastpref=request.form['roastpref']
        gender=request.form['gender']
        dob=request.form['dob']
        subscriber=0
        cursor.execute('SELECT * FROM user WHERE username = %s', (username))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'

        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)', (total_name,username, password, email,address,subscriber,dob,drinkfreq,roastpref,gender))
            conn.commit()
            msg = 'You have successfully registered!'
    # Show registration form with message (if any)

    return (render_template('register.html', msg=msg))

@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None) 
   session.pop('username', None)
   # Redirect to login page
   return (redirect(url_for('login')))
@app.route('/pythonlogin/home')
def home():
    if 'loggedin' in session:
        return (render_template('home.html', products=PRODUCTS))
    return (redirect(url_for('login')))
@app.route('/product/<key>')
def product(key):
    product = PRODUCTS[int(key)]
    print(key)
    print(product)
    if not product:
        abort(404)
    return (render_template('product.html', product=product))
if __name__ == '__main__':

    app.run(debug=True)


