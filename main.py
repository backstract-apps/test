from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()