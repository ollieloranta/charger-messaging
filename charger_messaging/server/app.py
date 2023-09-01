import json
import logging
from typing import List

from bson import json_util
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse

from .database import session_collection
from .models import Session

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger("API")

app = FastAPI()


@app.post("/session/")
async def add_session(session: Session):
    """Add session to the database

    :param data: Session data to be added
    :raises HTTPException: If input data is incorrect
    :return: string to simply inform data is added.
    """
    try:
        session_collection.insert_one(dict(session))
    except json.decoder.JSONDecodeError as err:
        logger.error(err)
        raise HTTPException(status_code=400, detail="Invalid request data")
    logger.info(f"Added: {session}")
    return "Session added."


@app.get("/session/", response_model=List[Session])
async def get_all_sessions():
    """Get all registered sessions

    :return: JSONResponse with each session's info
    """
    logger.info("Return all sessions.")
    # Get all sessions. Exclude MongoDB _id that is not json-serializable
    result = [res async for res in session_collection.find({}, {"_id": 0})]
    return JSONResponse(json.loads((json_util.dumps(result))))
