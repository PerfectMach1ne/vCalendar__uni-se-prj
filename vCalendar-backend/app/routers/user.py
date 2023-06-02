from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the ID {user_id} does not exist.")

    return user
    # db_user = crud.get_user(db, user_id=user_id)
    # if db_user is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return db_user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreate)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = user.password + "notrlyhashed"  # placeholder for JWT logic
    user.password = hashed_password  # placeholder for JWT logic

    # Create a new user; unpack the models dictionary
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    # new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
