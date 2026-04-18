from src.books.model import Book
from sqlalchemy.orm import Session

class BookRepo:

    @staticmethod
    def find_perId(id:int,user_id:int,db:Session):
        return db.query(Book).filter(Book.id == id , Book.user_id == user_id).first()
    @staticmethod
    def add(new_book:Book, db:Session):

        name = db.query(Book).filter(Book.title == new_book.title).first()

        if name:

            return {'status':'error','message':'Book already exists'}

        try:

            db.add(new_book)
            db.commit()
            db.refresh(new_book)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}


    @staticmethod
    def remove_book(id:int,user_id:int,db:Session):

        book = BookRepo.find_perId(id,user_id,db)

        if not book:
            return {'status':'error','message':'Book not found'}

        try:

            db.delete(book)
            db.commit()
            db.refresh(book)

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}

    @staticmethod
    def update_book(id:int,user_id:int,name:str,genre:str,description:str,db:Session):

        book = BookRepo.find_perId(id,user_id,db)

        if not book:
            return {'status':'error','message':'Book not found'}

        try:

            if name: book.name = name
            if genre: book.genre = genre
            if description:book.description = description

            db.commit()


        except Exception as e:

            return {'status':'error','message':str(e)}

