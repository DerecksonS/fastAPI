from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

## CHECK HOW TO IMPLEMENT ALEMBIC

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# http://127.0.0.1:8000/docs

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello Mariana"}
