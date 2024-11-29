# SQLAlchemy
SQLAlchemy practice - to define a table structure and interact with a SQLite database using ORM (Object-Relational Mapping).
Many-to-Many

## Features
- Create and manage a SQLite database.
- Define models for `Student` and `Course` with relationships.
- Implement a many-to-many association table (`student_course`).
- Populate the database with example data and link students to courses.

- Advanced Filtering: Query students enrolled in a specific course.
- Aggregations: Count the number of students in each course.
- Dynamic Enrollment: Enroll students based on certain criteria (e.g., students with fewer than X courses).
- Deleting Relationships: Allow un-enrolling a student from a course.
- Custom Queries: Write reusable functions to retrieve data efficiently.

## Key Components

1. **Base Class**:
   - [x] `Base` is defined using `declarative_base()` to serve as the base class for model definitions.

2. **Models**:
   - [x] `Student` class for a table in the database:
     - [x] `__tablename__`: Specifies the table name (`'students'`).
     - Columns:
       - [x] `id`: Integer, primary key.
       - [x] `name`: String.
       - [x] `email`: String.

       - [x] relationship for many-to-many association.

   - [x] `__repr__` method: Returns a string representation of `student` instances with attributes.


   - [x] `Course` class for a table in the database:
     - [x] `__tablename__`: Specifies the table name (`'courses'`).
     - Columns:
       - [x] `id`: Integer, primary key.
       - [x] `title`: String.
       - [x] `detail`: String.

       - [x] relationship for many-to-many association.


3. **Database Engine and Table Creation**:
   - [x] `engine = create_engine('sqlite:///instance/courses.db')`: Connection to database (`courses.db`).
   - [x] `Base.metadata.create_all(engine)`: Creates the tables if they don't already exist.
   - [x] `Association table`: foreign keys relating student to a course for each course registration

4. **Session Setup**:
   - [x] `Session = sessionmaker(bind=engine)`: Set up session factory.
   - [x] `session = Session()`: Session instance to interact with the database.


5. **Multiple tables and relationships**:
   - [x] single model / table
   - [x] multiple model. one to many relationship
   - [x] multiple model. many to many relationship

