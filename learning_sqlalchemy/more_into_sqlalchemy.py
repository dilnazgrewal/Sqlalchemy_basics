from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///school2.db", echo=True)
Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"[{self.id}] {self.name}"
    

enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True)

    courses = relationship("Course", secondary=enrollments, backref="students")

    def __repr__(self):
        return f"[{self.id}] {self.name} - Age {self.age} - {self.email}"
    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def enroll_student(student_id, course_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if student and course:
        student.courses.append(course)
        session.commit()

def unenroll_student(student_id, course_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if student and course and course in student.courses:
        student.courses.remove(course)
        session.commit()

def list_student_courses(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    return student.courses if student else []

# enroll_student(2, 2)          
# print(list_student_courses(2))

unenroll_student(1, 2)        # remove that enrollment
print(list_student_courses(1))