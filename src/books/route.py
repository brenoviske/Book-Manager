from fastapi import APIRouter , Depends , HTTPException , Form
from pydantic import BaseModel
from sqlalchemy.orm import Session

# -------- Imports within the folder ------ #

from src.books.model import Book
from src.books.controller import BookController
from src.database.config import get_db


# ------- Models responsive by Pydantic ------

class BookCreate(BaseModel):

    name: str
    genre: str
    description: str
    user_id:int


class BookUpdate(BaseModel):

    name: str
    genre: str
    description: str

router = APIRouter()


@router.post('/add')
def add_book(
        new : BookCreate,
        db:Session = Depends(get_db)
):

    book = Book(name = new.name, genre = new.genre, description = new.description , user_id = new.user_id)

    return BookController.add(book,db)

@router.delete('/delete')
def delete_book(
        id:int,
        db:Session = Depends(get_db)
):
    return BookController.delete(id,db)

@router.put('/update')
def update_book(
        id:int,
        user_id:int,
        bookUpdate:BookUpdate,
        db:Session = Depends(get_db)
):

    return BookController.update(id,user_id,bookUpdate.name, bookUpdate.genre,
                                 bookUpdate.description,db)




