from fastapi import FastAPI
from .routes import router

app = FastAPI(title="DevOps FastAPI Project")

@app.get("/")
def root():
    return {"message": "Welcome to DevOps FastAPI App"}

app.include_router(router)
