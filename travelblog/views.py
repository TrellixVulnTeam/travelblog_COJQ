from flask import Flask, render_template, flash, redirect, session, request, url_for
from .models import Member_table, db
import os
from travelblog import app
 
@app.route('/')

@app.route('/index.html')
def index():
    username = session.get('username', '')
    return render_template("index.html")

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/register.html', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['rusername']
        password = request.form['rpassword']
        name = request.form['rname']
        try:
            new_user = Member_table(account_name = name, username = username, password = password)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            session['password'] = password
            flash('Register Successfully', 'success')
            return redirect(url_for('.login'))
        except:
            db.session.rollback()
            error = "Username or Password already exists."
            flash('Something wrong!, please try again. ', 'error')
    return render_template("index.html", error=error)

