from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for book input
class Book(BaseModel):
    id: int
    title: str
    author: str 
    pages: int

# In-memory database

books = []

# ✅ Get all books

@app.get("/books")
def getbooks():
    return books

# ✅ Add a new book
@app.post("/books")
def create_book(book: Book):
      # Check if book with same ID already exists
    
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail = "Book with this ID ")
    books.append(book)
    return {"message": "Book Added", "book": book }


# 🔧 TODO: Get book by ID
@app.get("/books/{book_id}")
def get_books(book_id: int):
     
     # your code here
     pass


#  TODO: delete the by its id
@app.delete("/books/{book_id}")
def delete_book(book_id : int ):
    # Your code here
    pass


# Update book by id 
@app.put("/books/{book_id}")
def update_book(book_id: int , update_book: Book):
    # Your code here
    pass
