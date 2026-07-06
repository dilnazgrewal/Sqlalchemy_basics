import sqlite3

# Step 1: Connect (creates school.db file if it doesn't exist)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Step 2: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# Step 3: Insert a row
cursor.execute(
    "INSERT INTO students (name, age, email) VALUES (?, ?, ?)",
    ("Sehaj", 22, "s@mail.com")
)

# Step 4: COMMIT — this is new and important (explained below)
conn.commit()

# Step 5: Query it back
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(rows)

conn.close()