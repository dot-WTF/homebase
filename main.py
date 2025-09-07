import uvicorn
from fastapi import FastAPI
import os
from src.routes.wordle import wordle_routes
from src.database.connection import session

app = FastAPI()

app.include_router(wordle_routes.router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    
    
