from src.books.model import Book
from src.books.repo import BookRepo
from sqlalchemy.orm import Session


class BookController:

    @staticmethod
    def add(new_book:Book, db:Session):

        return BookRepo.add(new_book, db)

    @staticmethod
    def delete(id:int, db:Session):
        return BookRepo.remove_book(id,db)

    @staticmethod
    def update(id:int,name:str,genre:str,description:str, db:Session):
        return BookRepo.update_book(id, name, genre, description, db)

