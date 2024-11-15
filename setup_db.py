# imports

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# SQLAlchemy Many-To-Many

Base = declarative_base()

# Association table
student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # relationship
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

# course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String, nullable=False)

    # relationship
    students = relationship("Student", secondary=student_course, back_populates="courses")
    

engine = create_engine('sqlite:///courses.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

stud1 = Student(name="alice", email="alice@sample.com")
stud2 = Student(name="charl", email="charl@sample.com")
stud3 = Student(name="dory", email="dory@sample.com")
stud4 = Student(name="emma", email="emma@sample.com")

course1 = Course(title="History 101", details="history")
course2 = Course(title="Maths 101", details="maths")

course2.students.extend([stud1, stud4])
course1.students.extend([stud2, stud3, stud4])

session.add_all([stud1, stud2, stud3, stud4])
session.commit()

session.add_all([course1, course2])
session.commit()

session.close()