# library database program

# library database program

import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

cursor.execute("""
  CREATE TABLE books (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  year INTEGER,
  genre TEXT,
  copies INTEGER,
  rating INTEGER
  )
""")

cursor.execute(
    "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)",
    (1, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4, 5)
)

books = [
    (2, "Pride and Prejudice", "Jane Austen", 1813, "Fiction", 3, 5),
    (3, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction", 4, None),
    (4, "Dune", "Frank Herbert", 1965, "Science", 3, 5),
    (5, "The Silent Patient", "Alex Michaelides", 2019, "Mystery", 2, None),
    (6, "Sapiens", "Yuval Noah Harari", 2011, "History", 5, 4),
    (7, "Dracula", "Bram Stoker", 1897, "Horror", 3, 5),
    (8, "The Martian", "Andy Weir", 2011, "Science", 4, 4)
]

cursor.executemany(
    "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)",
    books
)

conn.commit()

print("\nBooks published after 1990:")

cursor.execute("SELECT title, author FROM books WHERE year > 1990")

results = cursor.fetchall()

for book in results:
    print(book[0], "-", book[1])

conn.close() 



print("\nFiction books with more than 2 copies:")

cursor.execute(
    "SELECT title FROM books WHERE genre = ? AND copies > ?",
    ("Fiction", 2)
) 



print("\nBooks published before 1900 OR rated 5:")

cursor.execute(
    "SELECT title FROM books WHERE year < ? OR rating = ?",
    (1900, 5)
)

results = cursor.fetchall()

for book in results:
    print(book[0])


results = cursor.fetchall()

for book in results:
    print(book[0])



print("\nBooks NOT in the Mystery genre:")

cursor.execute(
    "SELECT title FROM books WHERE NOT genre = ?",
    ("Mystery",)
)

results = cursor.fetchall()

for book in results:
    print(book[0])



print("\nBooks in Science or History:")

cursor.execute(
    "SELECT title FROM books WHERE genre IN (?, ?)",
    ("Science", "History")
)

results = cursor.fetchall()

for book in results:
    print(book[0])

letter = input("\nEnter a letter to search author names: ")

print("\nAuthors whose names start with " + letter + ":")

cursor.execute(
    "SELECT author FROM books WHERE author LIKE ?",
    (letter + "%",)
)

results = cursor.fetchall()

for author in results:
    print(author[0])



print("\nBooks with no rating:")

cursor.execute("SELECT title FROM books WHERE rating IS NULL")

results = cursor.fetchall()

for book in results:
    print(book[0])
conn.close()
