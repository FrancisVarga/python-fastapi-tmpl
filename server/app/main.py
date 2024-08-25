import os
from fastapi import FastAPI, HTTPException, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()

templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
)

# add health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}
    
# start uvicorn server within this script
if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, log_level="info")
