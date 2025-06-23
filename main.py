from fastapi import FastAPI, HTTPException
from models import Book
from database import books_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Library API"}

@app.post("/books/")
def add_book(book: Book):
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return {"message": "Book added successfully", "book": book}

@app.get("/books/")
def get_books():
    return books_db

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            books_db.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
