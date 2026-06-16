# FastAPI application for cloud project.
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cloud project is running"}

@app.get("/time")
def get_time():
    return {"time": str(datetime.utcnow())}

@app.get("/status")
def status():
    return {"status": "ok"}