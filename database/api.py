from fastapi import FastAPI

#import db_handler as db
import db_handler_sqlite as dbs

app = FastAPI()


@app.on_event("startup")
def startup():
    dbs.db_startup()


@app.on_event("shsutdown")
def shutdown():
    dbs.db_shutdown()

# push the item into the database
@app.post("/saveReport")
def insert_item(report: dbs.Report):
    #dbs.insert_report(report)
    print(report.url)


