from fastapi import FastAPI,File,UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
async def ping():
    return "Hello, I am alive"