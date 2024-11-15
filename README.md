# SQLAlchemy
SQLAlchemy practice - to define a table structure and interact with a SQLite database using ORM (Object-Relational Mapping).

## Key Components

1. **Base Class**:
   - [x] `Base` is defined using `declarative_base()` to serve as the base class for model definitions.

2. **User Model**:
   - [x] `User` class for a table in the database:
     - [x] `__tablename__`: Specifies the table name (`'users'`).
     - Columns:
       - [x] `id`: Integer, primary key.
       - [x] `username`: TEXT NOT NULL.
       - [x] `email`: TEXT NOT NULL.
       - [x] `age`: Integer, optional.
   - [x] `__repr__` method: Returns a string representation of `User` instances with attributes.

3. **Database Engine and Table Creation**:
   - [x] `engine = create_engine('sqlite:///example.db')`: Connection to database (`example.db`).
   - [x] `Base.metadata.create_all(engine)`: Creates the tables if they don't already exist.

4. **Session Setup**:
   - [x] `Session = sessionmaker(bind=engine)`: Set up session factory.
   - [x] `session = Session()`: Session instance to interact with the database.

5. **Adding New User**:
   - [x] `new_user = User(...)`: Creates a new `User` instance.
   - [x] `session.add(new_user)`: Adds the user to the session.
   - [x] `session.commit()`: Commits the transaction to save changes in the database.

6. **Multiple tables and relationships**:
   - [x] single model / table
   - [x] multiple model. one to many relationship
   - [ ] multiple model. many to many relationship

