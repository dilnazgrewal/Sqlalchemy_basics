from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# The "engine" = connection to the actual database file
engine = create_engine("sqlite:///school.db", echo=True)  # echo=True shows generated SQL!

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True)

# Create the table (only runs if it doesn't already exist)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#INSERTING NEW STUDENT
# new_student = Student(name="Nazu", age=20, email="n@mail.com")
# session.add(new_student)
# session.commit()

#UPDATING STUDENT
# student = session.query(Student).filter(Student.id == 4).first()
# student.email = "updated@mail.com"
# session.commit()

#DELETING STUDENT
# student = session.query(Student).filter(Student.id == 4).first()
# session.delete(student)
# session.commit()