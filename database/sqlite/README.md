## DATABASE CONFIGURATION & HANDLING
This folder contains all scripts that start and handle the database.<br />

**database.py** contains all the info about the db configuration (db URL, SQLAlchemy Engine and SessionLocal).<br />
**models.py** describes all the models used by the db.<br />
**db_handler** is the handler that operates directly with the db:
    - Item class: BaseModel used for the API call (url: str, reports: list);
    - insert_report(db: Session, item: Item): push a new set of reports into the db.
