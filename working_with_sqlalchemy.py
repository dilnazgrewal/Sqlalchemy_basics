from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# The "engine" = connection to the actual database file
engine = create_engine("sqlite:///school.db", echo=True)  # echo=True shows generated SQL!

Base = declarative_base()

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    subject_code = Column(Integer, unique=True)
    description = Column(String, unique=True)

    def __repr__(self):
        return f"[{self.id}] {self.name} - Code {self.subject_code} - {self.description}"

#Delete the table if it exists
# Subject.__table__.drop(engine, checkfirst=True)
# print("Table 'subjects' deleted successfully!")
#Create the table (only runs if it doesn't already exist)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_subject(name, subject_code, description):
    new_subject = Subject(name=name, subject_code=subject_code, description=description)
    session.add(new_subject)
    session.commit()

def update_subject(subject_id, name=None, subject_code=None, description=None):
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    if subject:
        if name is not None:
            subject.name = name
        if subject_code is not None:
            subject.subject_code = subject_code
        if description is not None:
            subject.description = description
        session.commit()

def delete_subject(subject_id):
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    if subject:
        session.delete(subject)
        session.commit()
        
def get_subjects():
    subjects = session.query(Subject).all()
    return subjects


add_subject("Math", 101, "Mathematics Basics")
add_subject("Science", 102, "Introduction to Science")
add_subject("History", 103, "World History Overview")
add_subject("English", 104, "English Literature and Grammar")

get_subjects_list = get_subjects()
for subject in get_subjects_list:
    print(f"ID: {subject.id}, Name: {subject.name}, Subject Code: {subject.subject_code}, Description: {subject.description}")

# delete_subject(3)  # Deletes the subject with ID 3 (History)

