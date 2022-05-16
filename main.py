from fastapi import FastAPI, Request, Response

from pydantic import BaseModel
from datetime import date, timedelta

app = FastAPI()
# to see what funny will come
app.counter = 0


class HelloResp(BaseModel):
    msg: str


@app.get('/counter')
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
    days_dict = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    if days_dict.get(name.lower()) == number:
        return Response(status_code=200)
    else:
        return Response(status_code=400)


# Task 1.4
app.event_id = 1
app.events = {}


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
        id=event_id,
        name=event.event,
        date=event.date,
        date_added=date_added
    )
    app.events[event_id] = event_out
    return event_out
