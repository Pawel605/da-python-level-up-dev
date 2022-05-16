import datetime
from datetime import date

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

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
        id=event_id,
        name=event.event,
        date=event.date,
        date_added=date_added
    )
    app.events.append(event_out)
    return event_out


# Task 1.5
@app.get("/event/{date}", status_code=200)
def get_event(date: str):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return Response(status_code=400)
    events_list = []

    for event in app.events:
        if datetime.datetime.strptime(date, '%Y-%m-%d').date() == event.date:
           events_list.append(event)

    if len(events_list) != 0:
        return events_list
    else:
        return Response(status_code=404)
