from sqlalchemy.orm import Session
from src.users.model import User
from src.users.repo import UserRepo


class UserController:

    @staticmethod
    def add(user:User, db:Session):
        return UserRepo.add_user(user, db)

    @staticmethod
    def remove(id:int,db:Session):
        return UserRepo.remove_user(id, db)

    @staticmethod
    def update(id:int,email:str,username:str,db:Session):
        return UserRepo.update_user(id, email, username, db)

    @staticmethod
    def login(email:str,password:str,db:Session):
        return UserRepo.user_login(email, password, db)


