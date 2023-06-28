from fastapi                    import FastAPI, Depends
from fastapi.middleware.cors    import CORSMiddleware
from sqlalchemy.orm             import Session
from starlette.responses        import RedirectResponse

from sqlite             import models, db_handler as dba
from sqlite.database   import SessionLocal, engine

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
def push_report(item: dba.Item, db: Session = Depends(get_db)):
    return dba.insert_report(db, item)



