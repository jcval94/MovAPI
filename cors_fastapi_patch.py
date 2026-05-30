"""
Snippet para habilitar CORS en FastAPI.

Colócalo en GCP/api/main.py después de crear `app = FastAPI(...)`.
Luego reconstruye y redespliega Cloud Run.
"""

import os
from fastapi.middleware.cors import CORSMiddleware

cors_origins_raw = os.getenv("MSMX_CORS_ORIGINS", "*")
cors_origins = [origin.strip() for origin in cors_origins_raw.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)
