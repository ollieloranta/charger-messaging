from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .database import session_collection
from .models import ManySessions
import json


app = FastAPI()

@app.post("/session/")
async def add_session(data: str = Body(...)):
    print(data)
    session = json.loads(data)
    session_collection.insert_one(session)
    return {"Status": "ok"}

@app.get("/session/", response_model=ManySessions)
async def get_all_sessions():
    result = [res async for res in session_collection.find()]
    return JSONResponse(jsonable_encoder(ManySessions(sessions=result)))
