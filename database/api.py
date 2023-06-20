from fastapi import FastAPI

import db_handler as db

app = FastAPI()

# test the api
@app.get("/")
def read_root():
    return {"Hello": "world!"}

# push the item into the database
@app.post("/saveReport")
def insert_item(report: db.Report):
    db.insertReport(report)


@app.post("/removeReport")
def remove_item(test_name: str, test_id: int):
    return db.removeReport(test_name, test_id)


@app.get("/getScores")
def get_scores(test_name: str):
    return db.getScores(test_name)