# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:27:03 2019

@author: noahd
"""
1
from datetime import datetime
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
pcol=PRODUCTS.columns
print(pcol)
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
            return (redirect(url_for('home')))
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
@app.route('/pythonlogin/home',methods=['GET', 'POST'])
def home():
    cart=pd.DataFrame()
    cart['coffee_id_k']=PRODUCTS
    #num_products=request.f
    #print(cart)
    if 'loggedin' in session:
        g=request.form.to_dict()
        if g:
            print(g)
            g1=tuple(g.items())
            idd=cursor.execute('SELECT user_id FROM user WHERE username = %s', [session['id']])
            f=[idd+1]*len(g1)
            cart_products=pd.DataFrame(list(g1),columns=['coffee_id_k','count'])
            cart_products['coffee_id_k']=pd.to_numeric(cart_products['coffee_id_k'])
            cart_products['coffee_id_k']+=1
            cart_products.insert(0,"user_id_k",f)
            cursor.execute('Truncate kart')
            conn.commit()
            for index, row in cart_products.iterrows():
                cursor.execute('INSERT INTO kart VALUES (%s, %s, %s)', (row['user_id_k'],row['coffee_id_k'],row['count']))
                conn.commit()
                print(1)
            #cart_products.to_sql('kart', engine, if_exists='replace')
            print(cart_products)

        cursor.execute('select coffee_id,title,roast,price,description from coffee_products right join rating on (coffee_id_r=coffee_id) where reviewer_id = %s order by rating desc',[session['id']])
        prods=cursor.fetchall()
        prods=pd.DataFrame(list(prods),columns=pcol)
        print(prods)
        prods=prods.to_dict('index')
        print(prods)
        msg = 'You have successfully added your products to the cart!'  
        return (render_template('home_products.html', username=session['username'],products=prods,msg=msg))
    return (redirect(url_for('login')))
@app.route('/product/<key>')
def product(key):
    product = PRODUCTS[int(key)]
    print(key)
    print(product)
    if not product:
        abort(404)
    return (render_template('product.html',username=session['username'], product=product))

@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
       # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE user_id = %s', [session['id']])
        account = cursor.fetchone()
        print(account)
        # Show the profile page with account info
        return (render_template('profile.html', account=account))
    # User is not loggedin redirect to login page
    return (redirect(url_for('login')))


@app.route("/pythonlogin/cart")
def cart():
    if 'loggedin' in session:
        cursor.execute("SELECT coffee_id from coffee_products")
        coffees=cursor.fetchall()
        defval=[i + tuple([0]) for i in coffees]
 

        cursor.execute("select coffee_id_k,num_in_cart from kart")
        num_in_cart = cursor.fetchall()
        if len(num_in_cart)>0:
            cf=num_in_cart
        else:
            cf=defval
    
        print(num_in_cart)
        totalPrice = 0

        return(render_template('cart.html',products=PRODUCTS,cart_total=cf))
        #return (render_template("cart.html", products = products, totalPrice=totalPrice, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems)
    return (redirect(url_for('login')))

@app.route("/pythonlogin/checkout")
def checkout():
    if 'loggedin' in session:
        cursor.execute("SELECT * from kart where user_id_k = %s", [session['id']])
        coffees=cursor.fetchall()
        
        print(coffees)
        cursor.execute("Insert into orders values (null,%s,%s)", ( datetime.now().date(),[session['id']]))
       # num_in_cart = cursor.fetchall()
        conn.commit()
        cursor.execute("select * from kart where user_id_k = %s and num_in_cart>0",[session['id']])
        bought=cursor.fetchall()
        print(bought)
        cursor.execute("select order_id from orders where user_id_o =%s order by order_date desc limit 1",[session['id']])
        orderid=cursor.fetchall()
        print(orderid)
        coffee_o=[]
        coffee_kind=[]
        coffee_kind_count=[]
        for i in range(0,len(bought)):
            cursor.execute('insert into coffee_order values (%s,%s)',(bought[i][1],orderid[0][0]))
            #cursor.execute('insert into coffee_order values (%s,%s,%s)'(bought[i][1],orderid[0][0],bought[i][2]))
            coffee_o.append(orderid[0][0])
            coffee_kind.append(bought[i][1])
            coffee_kind_count.append(bought[i][2])
        # num_in_cart = cursor.fetchall()
        cursor.execute
        conn.commit()
        cursor.execute("update kart set num_in_cart =0 where user_id_k = %s", [session['id']])
        conn.commit()
        cursor.execute("select coffee_id_k,num_in_cart from kart")
        num_in_cart = cursor.fetchall()
        print(num_in_cart)
        cf=num_in_cart
        
 
        totalPrice = 0

        return(render_template('cart.html',products=PRODUCTS,cart_total=cf))
        #return (render_template("cart.html", products = products, totalPrice=totalPrice, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems)
    return (redirect(url_for('login')))



@app.route('/pythonlogin/review',methods=['GET', 'POST'])
def review():
    cart=pd.DataFrame()
    cart['coffee_id_k']=PRODUCTS
    #num_products=request.f
    #print(cart)
    if 'loggedin' in session:
        g=request.form.to_dict()
        if g:
            print(g)
            g1=tuple(g.items())
            idd=cursor.execute('SELECT user_id FROM user WHERE username = %s', [session['id']])
            f=[idd+1]*len(g1)
            cart_products=pd.DataFrame(list(g1),columns=['coffee_id_k','rating'])
            cart_products['coffee_id_k']=pd.to_numeric(cart_products['coffee_id_k'])
            cart_products['coffee_id_k']+=1
            cart_products.insert(0,"user_id_k",f)
            for i in range(len( cart_products['coffee_id_k'])):
                if int(cart_products['rating'][i])>0:
                    
                        cursor.execute('update rating set rating = %s where reviewer_id= %s and coffee_id_r=%s',(str(cart_products['rating'][i]),[session['id']],str(cart_products['coffee_id_k'][i])))
                        conn.commit()
                    #else:
                     #   cursor.execute('insert into rating values (%s,%s,%s)',([session['id']],str(cart_products['coffee_id_k'][i]),str(cart_products['rating'][i])))
                      #  conn.commit()
                    #cart_products.to_sql('rating',engine,if_exists='replace')
                    #cart_products.to_sql('kart', engine, if_exists='replace')
            print(cart_products)
            
        msg = 'You have successfully added your products to the cart!'  
        return (render_template('review.html', username=session['username'],products=PRODUCTS,msg=msg))
    return (redirect(url_for('login')))


if __name__ == '__main__':

    app.run(debug=True)


