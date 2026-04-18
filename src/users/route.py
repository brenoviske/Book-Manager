from fastapi import APIRouter, Depends, HTTPException, Form
from pydantic import BaseModel
from sqlalchemy.orm import Session

# -------Imports within the folder ------

from src.users.model import User
from src.users.controller import UserController
from src.database.config import get_db

router = APIRouter()

class UserCreate(BaseModel):

    email:str
    username:str
    password:str

class UserLogin(BaseModel):

    emall:str
    password:str

class UserUpdate(BaseModel):

    email:str
    username:str


# ----------- Routes ----------

@router.post('/add')
def add(
        new_user:UserCreate,
        db: Session = Depends(get_db),
):

    new_user = User(
        email = new_user.email,
        username=new_user.username,
        password=new_user.password
    )

    return UserController.add(new_user,db)

@router.post('/login')
def login(
    user_login:UserLogin,
    db:Session = Depends(get_db),
):

    return UserController.login(
        user_login.emall,
        user_login.password,
        db
    )

@router.delete('/delete')
def delete(
        id:int ,
        db:Session = Depends(get_db)
):
    return UserController.remove(id,db)

@router.put('/update')
def update(
        new_user:UserUpdate,
        db:Session = Depends(get_db),
):

    return UserController.update(new_user,db)