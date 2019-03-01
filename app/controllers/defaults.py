from app import app, lm, db
from flask import flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from app.models.tables import User
from app.models.forms import LoginForm, RegisterForm


@lm.user_loader
def load_user(id_):
  return User.query.filter_by(id_=id_).first()


@app.route('/')
@app.route('/home')
def home():
  return render_template('home/index.html')


@app.route('/about')
def about():
  return render_template('about/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.password == form.password.data:
      login_user(user)
      return redirect(url_for('home'))
    else:
      flash('User Name or Password Incorrect')
  return render_template('login/index.html', form=form)


@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    name = form.name.data
    username = form.username.data
    email = form.email.data
    password = form.password.data
    user = User(username, password, name, email)
    try:
      db.session.add(user)
      db.session.commit()
    except:
      flash('Username or Email is already in use')
    return redirect(url_for('login'))
  return render_template('register/index.html', form=form)
