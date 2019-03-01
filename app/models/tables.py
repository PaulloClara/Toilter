from app import db


class User(db.Model):
  __tablename__ = 'users'

  id_ = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, unique=True)
  password = db.Column(db.String)
  name = db.Column(db.String)
  email = db.Column(db.String, unique=True)

  @property
  def is_authenticated(self):
    return True

  @property
  def is_active(self):
    return True

  @property
  def is_anonymous(self):
    return False

  def get_id(self):
    return str(self.id_)

  def __init__(self, username, password, name, email):
    self.username = username
    self.password = password
    self.name = name
    self.email = email

  def __repr__(self):
    return f'<User {self.username}>'


class Post(db.Model):
  __tablename__ = 'posts'

  id_ = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text)
  userId = db.Column(db.Integer, db.ForeignKey('users.id_'))
  userP = db.relationship('User', foreign_keys=[userId])

  def __init__(self, content, userId):
    self.content = content
    self.userId = userId

  def __repr__(self):
    return f'<Post {id_}>'


class Follow(db.Model):
  __tablename__ = 'follow'

  id_ = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('users.id_'))
  followId = db.Column(db.Integer, db.ForeignKey('users.id_'))
  userF = db.relationship('User', foreign_keys=[userId])
  userFF = db.relationship('User', foreign_keys=[followId])

