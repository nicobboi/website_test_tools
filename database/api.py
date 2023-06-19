from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

import db_handler as db

app = FastAPI()

# test the api
@app.get("/")
def read_root():
    return {"Hello": "world!"}

# push the item into the database
@app.post("/pushReport")
def insert_item(report: db.Report):
    db.insertReport(report)
    return PlainTextResponse(content="Report successfully inserted into the database.")

@app.post("/removeReport")
def remove_item(test_name: str, test_id: int):
    return db.removeReport(test_name, test_id)
    #return PlainTextResponse(content="Report successfully removed from the database.")