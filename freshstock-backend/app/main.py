from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as api_v1_router


app = FastAPI(
    title="FreshStock API",
    description="Backend API for FreshStock",
    version="1.0.0",
)


# Allow the Vite frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API v1 routes
app.include_router(
    api_v1_router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": "FreshStock API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }