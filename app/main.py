import uvicorn

from app.routes.endpoints import api

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, port=8080, log_level="info")
