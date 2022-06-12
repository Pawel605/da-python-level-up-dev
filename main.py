import datetime
from datetime import date

from fastapi import FastAPI, Depends, status, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from pydantic import BaseModel

from app.views import router as northwind_api_router
from utils import calculate_age


app = FastAPI()
app.include_router(northwind_api_router, tags=["northwind"])

# to see what funny will come
app.counter = 0


class HelloResp(BaseModel):
    msg: str


@app.get("/counter")
def counter():
    app.counter += 1
    return str(app.counter)


@app.get("/hello/{name}", response_model=HelloResp)
async def read_item(name: str):
    return HelloResp(msg=f"Hello {name}")


# Task 1.1
@app.get("/")
def root():
    return {"start": "1970-01-01"}


# Task 1.2
@app.get("/method", status_code=200)
@app.post("/method", status_code=201)
@app.delete("/method", status_code=200)
@app.put("/method", status_code=200)
@app.options("/method", status_code=200)
def read_request(request: Request):
    return {"method": request.method}


# Task 1.3
@app.get("/day")
def check_day_number(name: str, number: int):
    days_dict = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7,
    }

    if days_dict.get(name.lower()) == number:
        return Response(status_code=200)
    else:
        return Response(status_code=400)


# Task 1.4
app.event_id = 1
app.events = []


class EventIn(BaseModel):
    date: str
    event: str


class EventOut(BaseModel):
    id: int
    name: str
    date: date
    date_added: date


@app.put("/events", status_code=200)
def put_event(event: EventIn):
    event_id = app.event_id
    app.event_id += 1

    date_added = date.today().strftime("%Y-%m-%d")

    event_out = EventOut(
        id=event_id, name=event.event, date=event.date, date_added=date_added
    )
    app.events.append(event_out)
    return event_out


# Task 1.5
@app.get("/events/{date}", status_code=200)
def get_event(date: str):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return Response(status_code=400)
    events_list = []

    for event in app.events:
        if datetime.datetime.strptime(date, "%Y-%m-%d").date() == event.date:
            events_list.append(event)

    if len(events_list) != 0:
        return events_list
    else:
        return Response(status_code=404)


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
    header = request.headers.get("User-Agent")

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


# Task 3.4

app.list_of_strings = []


@app.delete("/save/{string}")
@app.get("/save/{string}")
@app.put("/save/{string}")
def save_data(request: Request, string: str = ""):
    method = request.method

    if method == "PUT":
        if string not in app.list_of_strings:
            app.list_of_strings.append(string)
        return Response(status_code=status.HTTP_200_OK)
    elif method == "GET":
        if string in app.list_of_strings:
            return RedirectResponse(
                url="/info",
                headers={"Location": "/info"},
                status_code=status.HTTP_301_MOVED_PERMANENTLY,
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="String not found!",
            )
    elif method == "DELETE":
        if string in app.list_of_strings:
            app.list_of_strings.remove(string)
            return Response(status_code=status.HTTP_200_OK)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Method not allowed!",
        )
