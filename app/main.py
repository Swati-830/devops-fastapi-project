from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI DevOps Project"}

app.include_router(router)

