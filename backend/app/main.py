from fastapi import FastAPI

app = FastAPI(
    title="DocQuery API",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}    
@app.get("/")
def homepage():
    return {"message": "welcome to the homepage"}