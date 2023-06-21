from fastapi                    import FastAPI, Depends, HTTPException
from fastapi.middleware.cors    import CORSMiddleware
from sqlalchemy.orm             import Session
from starlette.responses        import RedirectResponse

from .sqlite            import models, schemas, db_handler as dba
from .sqlite.database   import SessionLocal, engine

from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_creadentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# API

# redirect to SwaggerUI
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/saveReport")
def push_report(report: dba.Report, db: Session = Depends(get_db)):
    return dba.insert_report(db, report)


'''
@app.on_event("startup")
def startup():
    dbs.db_startup(engine)


@app.on_event("shsutdown")
def shutdown():
    dbs.db_shutdown()


# push the item into the database
@app.post("/saveReport")
def insert_item(report: Report):
    #dbs.insert_report(report)
    print(report.url)
'''


