from tinydb import TinyDB, where
from datetime import datetime
from pydantic import BaseModel
import os

class Report(BaseModel):
    name: str
    url: str
    type: str
    tool: str
    stats: dict | None
    notes: dict | None
    documents: dict | None

# Function to push a report into the database
def insertReport(report: Report):
    db_path = os.path.dirname(__file__) + "/reports_db.json"

    db = TinyDB(db_path, indent=4, separators=(',', ': '))
    table = db.table(report.name)

    element = {
        "url": report.url,
        "type": report.type,
        "tool": report.tool,
        "stats": report.stats,
        "notes": report.notes,
        "documents": report.documents,
        "timestamp": str(datetime.now())
    }

    table.insert(element)

# Function to remove a report in the database
def removeReport(test_name: str, test_id: int):
    db_path = os.path.dirname(__file__) + "/reports_db.json"

    db = TinyDB(db_path, indent=4, separators=(',', ': '))
    # check if the given table exists
    if not test_name in db.tables():
        return "Table with the given name doesn't exist."
    table = db.table(test_name)

    if table.contains(doc_id=test_id):
        table.remove(doc_ids=[test_id])
        return "Report removed."
    

    return "Report with the given id doesn't exist."
    


