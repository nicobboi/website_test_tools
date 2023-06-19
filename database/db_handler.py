from tinydb import TinyDB
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


