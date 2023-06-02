from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db
from .routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)

@app.get("/")  # Decorator that turns root() into an API path operation
def root():
    return {"root_message": "helo world"}
# if __name__ == "__main__":
#     create_connection(r"D:\Programming\uni-se-prj\vCalendar-backend\database\maindb.db")
