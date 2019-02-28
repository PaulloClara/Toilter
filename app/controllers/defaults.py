from app import app
from flask import flash, redirect, url_for, render_template


@app.route('/')
@app.route('/home')
def index():
  return render_template('home/index.html')


@app.route('/about')
def about():
  return render_template('about/index.html')


@app.route('/login')
def login():
  return render_template('login/index.html')


@app.route('/logout')
def logout():
  return redirect(url_for('index'))
