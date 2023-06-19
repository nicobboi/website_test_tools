from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from db_handler import insertReport, Report

app = FastAPI()

# test the api
@app.get("/")
def read_root():
    return {"Hello": "world!"}

# push the item into the database
@app.post("/pushItem")
def insert_item(report: Report):
    insertReport(report)
    return PlainTextResponse(content="Data successfully inserted into the database!")