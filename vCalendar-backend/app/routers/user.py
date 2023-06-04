from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from .. import models, schemas, oauth2, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user_byid(user_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the ID {user_id} does not exist.")

    return user
    # db_user = crud.get_user(db, user_id=user_id)
    # if db_user is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return db_user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    password_to_hash = utils.hash_pwd(user.hashed_password)
    user.hashed_password = password_to_hash  # placeholder for JWT logic

    # Create a new user; unpack the models dictionary
    new_user = models.User(**user.dict())

    user_check = db.query(models.User).filter(models.User.email == new_user.email).first()

    if not(user_check is None):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with the email {new_user.email} already exists!")
    # The BAD (I tried):
    # new_user = models.User(email=user.email, hashed_password=user.hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
