# imports

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from random import randint, choice, sample

DATABASE = 'sqlite:///instance/courses.db'

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
    detail = Column(String, nullable=False)

    # relationship
    students = relationship("Student", secondary=student_course, back_populates="courses")
    
    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title})"

def main():
    engine = create_engine(DATABASE)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # add_sample_students(session)
    # add_sample_courses(session)
    # add_sample_enrollments(session)

    students_in_course(session, 'physics101')
    course_enrollment_counts(session)
    enroll_students_dynamically(session, max_course_count=2)
    withdraw_from_course(session, student_name = 'Hazel', course_title = 'finance101')

    session.commit()
    session.close()

def add_sample_students(session):
    name_list = ['Elijah', 'Theodore', 'Harper', 'Henry', 'Oliver', 'Barbara', 
                    'Liam', 'Evelyn', 'Amelia', 'Isabella', 'Mia', 'James', 'Noah', 
                    'Jennifer', 'Hazel', 'Luna'
    ]

    for name in name_list:
        email = f"{name}@sample.com"

        student = Student(name=name, email=email)
        session.add(student)

def add_sample_courses(session):
    titles = ['maths101', 'physics101', 'geography101', 'chemistry101', 'finance101', 'biology101']

    for title in titles:
        detail = f"{title} course details"

        course = Course(title=title, detail=detail)

        session.add(course)


def add_sample_enrollments(session):
    students = session.query(Student).all()
    courses = session.query(Course).all()  
    
    for student in students:
        course_count = choice([1,2,3,4])
        selected_courses = sample(courses, k=course_count)

        for course in selected_courses:
            if course not in student.courses:
                student.courses.append(course)


def students_in_course(session, course_title):
    course = session.query(Course).filter(Course.title==course_title).first()
    
    if course:
        enrolled_students = [student.name for student in course.students]
        print(f"{course.title}: {enrolled_students}")
    else:
        print(f"No course with title {course_title} found.")


def course_enrollment_counts(session):
    counts = (session.query(Course.title, func.count(student_course.c.course_id))
              .join(student_course, Course.id == student_course.c.course_id)
              .group_by(Course.title)
              .all()              
    )

    # print(counts)
    for title, count in counts:
        print(f"{title}: {count}")

def enroll_students_dynamically(session, max_course_count):
    students = session.query(Student).all()
    courses = session.query(Course).all()

    for student in students:
        if len(student.courses) <= max_course_count:
            remaining_courses = [course for course in courses if course not in student.courses]

            if remaining_courses:
                new_course = choice(remaining_courses)
                student.courses.append(new_course)
                print(f"{student.name} enrolled in {new_course.title}")

def withdraw_from_course(session, student_name, course_title):
    student = session.query(Student).filter(Student.name==student_name).first()
    course = session.query(Course).filter(Course.title==course_title).first()

    if student and course and course in student.courses:
        student.courses.remove(course)
        print(f"{student.name} withdrew from {course.title}")
    else:
        print("Invalid student or course detail")



if __name__ == "__main__":
    main()

