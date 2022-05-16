from fastapi import FastAPI, Request

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


# task 1.2
@app.get("/method", status_code=200)
@app.post("/method", status_code=201)
@app.delete("/method", status_code=200)
@app.put("/method", status_code=200)
@app.options("/method", status_code=200)
def read_request(request: Request):
    return {"method": request.method}

