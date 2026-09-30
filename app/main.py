from fastapi import FastAPI, 
from routers import qr

app = FastAPI()

app.include_router(qr.router)


@app.get("/")
async def root():
    return {"message":"todo bien"}