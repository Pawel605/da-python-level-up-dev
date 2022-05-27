import datetime
from datetime import date

from fastapi import FastAPI, Depends, status, HTTPException, Request
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
)
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from utils import calculate_age

app = FastAPI()


# Task 3.1
@app.get("/start", response_class=HTMLResponse)
def read_root_start():
    return """<h1>The unix epoch started at 1970-01-01</h1>"""


# Task 3.2
@app.post("/check", response_class=HTMLResponse)
def user_authorization(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    try:
        datetime.datetime.strptime(credentials.password, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password, correct date format is YYYY-MM-DD",
        )

    date_of_birth = date.fromisoformat(credentials.password)
    user_age = calculate_age(date_of_birth)

    if user_age < 16:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are under 16 years of age!",
        )
    else:
        return f"""<h1>Welcome {credentials.username}! You are {user_age}</h1>"""


# Task 3.3
@app.get("/info", status_code=status.HTTP_200_OK)
def get_info(request: Request, format: str = ""):
    header = request.headers.get('User-Agent')

    if format == "json":
        data = {"user_agent": f"{header}"}
        return JSONResponse(data)
    elif format == "html":
        data = f"""<input type="text" id=user-agent name=agent value="{header}">"""
        return HTMLResponse(data)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Format param is bad or empty! Param can only be in json or html format.",
        )
