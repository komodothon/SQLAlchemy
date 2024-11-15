# imports

import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


# sqlite raw codes

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS users_sql (
                id INTEGER PRIMARY KEY, 
                username TEXT NOT NULL, 
                email TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS posts_sql (
                post_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users_sql (id)
    );
""")

cursor.execute("INSERT INTO users_sql (id, username, email) VALUES (?, ?, ?)", (4, 'Alice', 'alice@samplecom'))
cursor.execute("INSERT INTO posts_sql (post_id, title, content, user_id) VALUES (?, ?, ?, ?)", (2, 'Today\'s rains', 'content content content', 4))

connection.commit()
connection.close()

# SQLAlchemy 

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    # define columns for table
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
class Post(Base):
    __tablename__ = 'posts'

    # define columns
    post_id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="posts")

    

engine = create_engine('sqlite:///example.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user1 = User(username='Bob', email='Bob@example.com')
print(new_user1)
session.add(new_user1)
session.commit()

user = session.query(User).filter_by(username='Bob').first()

post1 = Post(title='First post', content='content in 1st post', author=user)
session.add(post1)
session.commit()

post2 = Post(title='Second post', content=' 2nd post content')
user.posts.append(post2)
session.commit()

session.close()