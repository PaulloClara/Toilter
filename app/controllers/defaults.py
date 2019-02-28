from app import app
from flask import flash, redirect, url_for, render_template


@app.route('/')
@app.route('/home')
def index():
  return 'Home'


@app.route('/login')
def login():
  return 'Login'


@app.route('/logout')
def logout():
  return 'Logout'
