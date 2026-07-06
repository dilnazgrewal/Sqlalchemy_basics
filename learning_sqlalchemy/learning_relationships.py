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

# Create students and courses
g = Student(name="Gurpartap", age=22, email="gurpartap@mail.com")
d = Student(name="Dilnaz", age=21, email="dilnaz@mail.com")

math = Course(name="Math")
science = Course(name="Science")

# # Enroll them — just append to the list!
g.courses.append(math)
g.courses.append(science)
d.courses.append(math)

session.add_all([g, d, math, science])
session.commit()