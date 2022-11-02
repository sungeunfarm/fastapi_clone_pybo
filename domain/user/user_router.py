from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud,user_schema

router = APIRouter(prefix="/api/user",)

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create:user_schema.UserCreate,db:Session = Depends(get_db)):
    user = user_crud.get_exissting_user(db,user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="이미 존재하는 사용자 입니다.")
    
    user_crud.create_user(db=db,user_creat=_user_create)
