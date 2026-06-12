from fastapi import FastAPI
from database import get_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NAGP Assignment"}

@app.get("/employees")
def employees():
    return get_data()