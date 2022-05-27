from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# Task 3.1
@app.get("/start", response_class=HTMLResponse)
def read_root_start():
    return """<h1>The unix epoch started at 1970-01-01</h1>"""
