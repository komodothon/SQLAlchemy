from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    # define columns for table
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', age='{self.age}')>"
    

engine = create_engine('sqlite:///example.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(username='alice', email='alice@example.com', age=25)
print(new_user)

session.add(new_user)

session.commit()