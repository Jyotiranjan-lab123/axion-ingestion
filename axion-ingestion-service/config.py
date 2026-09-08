"""
Axion Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    # Example: postgresql://postgres:postgres@localhost:5432/axiondb
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
         "postgresql://admin:Password@12345@10.244.0.48:5432/axiondbb"
    )

settings = Settings()
