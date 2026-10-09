from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import qr_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(qr_route.router)


@app.get("/")
async def root():
    return {"message":"IT'S OKEY"}