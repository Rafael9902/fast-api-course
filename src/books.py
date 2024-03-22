from fastapi import FastAPI
from data.books import BOOKS

app = FastAPI()

@app.get('/books')
async def getBooks():
    return BOOKS