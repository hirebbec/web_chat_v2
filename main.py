from typing import List

import uvicorn
from fastapi import FastAPI

from routes.routes import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app)
