from fastapi                    import FastAPI, Depends
from fastapi.middleware.cors    import CORSMiddleware
from sqlalchemy.orm             import Session
from starlette.responses        import RedirectResponse

import models, db_handler as dba
from database                   import SessionLocal, engine

from datetime                   import datetime

# Creates database from models module description
models.Base.metadata.create_all(bind=engine)

# Start a new app API
app = FastAPI()

# API middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Get current db local session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



# --- API calls ---------------------------------------------------- #

# redirect to SwaggerUI
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# push a new set of reports into the db 
@app.post("/saveReport")
def insert(item: dba.Item, db: Session = Depends(get_db)):
    return dba.insert_reports(db, item)

# delete a report or all report of a site by its ID
@app.post("/deleteItem")
def delete(report_id: int = None, site_id: int = None, db: Session = Depends(get_db)):
    return dba.delete_item(db, report_id, site_id)

# get all scores from all reports of a specific site (url), (optional: get scores between timestamps)
@app.get("/getScores")
def scores(url: str, start: datetime = None, end: datetime = None, db: Session = Depends(get_db)):
    return dba.get_scores(db, url, start, end)
