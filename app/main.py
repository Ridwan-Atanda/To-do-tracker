from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, users, auth
from fastapi.middleware.cors import CORSMiddleware



# models.Base.metadata.create_all(bind=engine) ###this commands is not needed anymore 

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


###grab the router object fro the post and user file in routers folder 
app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)


