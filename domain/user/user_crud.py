from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def create_user(db:Session , user_creat:UserCreate):
    db_user = User(username=user_creat.username,password=pwd_context.hash(user_creat.password1),email=user_creat.email)

    db.add(db_user)
    db.commit()

def get_exissting_user(db:Session,user_create:UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) | 
        (User.email  == user_create.email)).first()