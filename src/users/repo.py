from sqlalchemy.orm import Session
from src.users.model import User
from src.auth.security import check_password


class UserRepo:

    @staticmethod
    def find_perId(id:int , db:Session):

        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def add_user(new_user:User,  db:Session):

        existing_email = db.query(User).filter(User.email == new_user.email).first()
        existing_username = db.query(User).filter(User.email == new_user.email).first()

        if existing_username:
            return {'status':'error','message':'Username already exists'}

        if existing_email:
            return {'status':'error','message':'Email already exists'}

        try:

            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            return {'status':'success'}


        except Exception as e:

            return {'status':'error','message':str(e)}


    @staticmethod
    def remove_user(id:int,db:Session):

        user = UserRepo.find_perId(id,db)

        if not user:
            return {'status':'error','message':'User not found'}

        try:

            db.delete(user)
            db.commit()
            return {'status':'success'}

        except Exception as e:
            return {'status':'error','message':str(e)}


    @staticmethod
    def update_user(id:int , email:str, username:str, db:Session):

        user = UserRepo.find_perId(id,db)

        if not user:
            return {'status':'error','message':'User not found'}

        try:
            if email :
                user.email = email

            if username:
                user.username = username

            db.commit()

            return {'status':'success'}

        except Exception as e:

            return {'status':'error','message':str(e)}


    @staticmethod
    def user_login(email:str, password:str, db:Session):

        existing_email = db.query(User).filter(User.email == email).first()

        if existing_email and check_password(password,existing_email.password_hash):

            return {'status':'success'}

        return {'status':'error','message':'Invalid credentials'}