import logging
import json

from fastapi import FastAPI, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .database import session_collection
from .models import ManySessions


app = FastAPI()

logger = logging.getLogger("API")


@app.post("/session/")
async def add_session(data: str = Body(...)):
    try:
        session = json.loads(data)
        session_collection.insert_one(session)
    except json.decoder.JSONDecodeError as err:
        logger.error(err)
        raise HTTPException(status_code=400, detail="Invalid request data")
    logger.info(f"Added: {session}")
    return "Session added."


@app.get("/session/", response_model=ManySessions)
async def get_all_sessions():
    logger.info("Return all sessions.")
    result = [res async for res in session_collection.find()]
    return JSONResponse(jsonable_encoder(ManySessions(sessions=result)))
