from fastapi import FastAPI

from src.upload.router import router as upload_router
from src.watch.router import router as watch_router

app = FastAPI(title="TODO")

app.include_router(upload_router, prefix="/upload")
app.include_router(watch_router, prefix="/watch")
