from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "HR-Tech AI API is working!"}
