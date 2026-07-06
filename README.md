# FastAPI + SQLAlchemy + SQLite CRUD API

A beginner-friendly REST API built using **FastAPI**, **SQLAlchemy**, and **SQLite**. This project demonstrates how to integrate an ORM with FastAPI to perform basic CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

- Create new records
- Retrieve all records
- Retrieve a record by ID
- Update existing records
- Delete records
- SQLAlchemy ORM integration
- SQLite database
- Pydantic request and response validation
- Interactive API documentation with Swagger UI

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## 📁 Project Structure

```text
.
├── database/
│   ├── school.db
│   └── school2.db
│
├── learning_sqlalchemy/
│   ├── sqlalchemy_basics.py
│   ├── working_with_sqlalchemy.py
│   ├── working_with_sqlite3.py
│   ├── learning_relationships.py
│   └── more_into_sqlalchemy.py
│
├── mini_database_app/
│   ├── __init__.py
│   ├── .gitignore
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

2. Navigate to the project directory:

```bash
cd your-repository-name
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn mini_database_app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

## 🗄️ Database

This project uses **SQLite** as the database and **SQLAlchemy** as the ORM.

The database tables are created automatically when the application starts if they do not already exist.

> **Note:** The SQLite database file is included in this repository for reference.

## 📚 Learning Objectives

This project was built to learn:

- FastAPI fundamentals
- REST API development
- SQLAlchemy ORM
- Database models and schemas
- CRUD operations
- Request validation using Pydantic
- Connecting FastAPI with a relational database

## 🤝 Contributing

Feel free to fork this repository, explore the code, and suggest improvements.

## 📄 License

This project is intended for learning and educational purposes.