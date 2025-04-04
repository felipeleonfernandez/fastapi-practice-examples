from fastapi import FastAPI

# FastAPI instance creation
app = FastAPI()

# Path operation decorator, in this case using GET method in root path
@app.get("/")
# Path operation function, in this case async and named root
async def root():
    return {"message": "Hello World"}