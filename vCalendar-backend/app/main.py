from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException

from . import models
from .database import engine
from .routers import auth, user

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


app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")  # Decorator that turns root() into an API path operation
def root():
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
                        detail=f"helo world!!!!! I'm a teapot. I swear.")
# if __name__ == "__main__":
#     create_connection(r"D:\Programming\uni-se-prj\vCalendar-backend\database\maindb.db")
