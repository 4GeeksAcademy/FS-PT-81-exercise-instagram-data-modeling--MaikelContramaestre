import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('users.id'))
    to_id = Column(Integer, ForeignKey('users.id'))
    user_from_id = relationship ('Users' , foreign_keys = [from_id] , backref='Follower')
    user_to_id = relationship ('Users' , foreign_keys = [to_id] , backref='Followed')



class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(),nullable=False)
    email = Column(String, unique=True)


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250),nullable=False)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', backref='posts')

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', backref='comments')
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship('Post', backref='comments')

class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    src = Column(String, nullable=False)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship('Post', backref='comments')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
