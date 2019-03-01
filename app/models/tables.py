from app import db


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.String, unique=True)
  password = db.Column(db.String)
  name = db.Column(db.String, unique=True)
  email = db.Column(db.String, unique=True)

  def __init__(self, userName, password, name, email):
    self.id = id
    self.userName = userName
    self.password = password
    self.name = name
    self.email = email

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
    return str(self.id)

  def __repr__(self):
    return f'<User {self.userName}>'


class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'))
  userP = db.relationship('User', foreign_keys=[userId])

  def __init__(self, content, userId):
    self.id = id
    self.content = content
    self.userId = userId

  def __repr__(self):
    return f'<Post {self.userId}>'


class Follow(db.Model):
  __tablename__ = 'follow'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('users.id'))
  followId = db.Column(db.Integer, db.ForeignKey('users.id'))
  userF = db.relationship('User', foreign_keys=[userId])
  userFF = db.relationship('User', foreign_keys=[followId])

