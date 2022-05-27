import datetime

from fastapi import FastAPI, Depends, security, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from datetime import date
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
