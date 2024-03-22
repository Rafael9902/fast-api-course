from fastapi import FastAPI
from data.books import BOOKS

app = FastAPI()

@app.get('/books')
async def get_books():
    return BOOKS

# path parameters are request parameters attached to the url
@app.get('/books/{book_title}')
async def get_params(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
