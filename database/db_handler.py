from tinydb import TinyDB, where, Query
from datetime import datetime
from pydantic import BaseModel
import os

class Report(BaseModel):
    url: str
    type: str
    tool: str
    stats: dict | None
    notes: dict | None
    documents: dict | None

db_path = os.path.dirname(__file__) + "/reports_db.json"

# run this script to setup a default database
def setupDB():
    db = TinyDB(db_path, indent=4, separators=(',', ': '))
    db.drop_tables()
    db.truncate()

# Function to push a report into the database
def insertReport(report: Report):
    db = TinyDB(db_path, indent=4, separators=(',', ': '))

    # tabella corrisponde ai test su un link specifico
    table = db.table(report.url)
    # se non esiste (mai fatti test su quel link), la popolo con le sue proprieta'
    '''
    if not table:
        table.insert({
            "performance": [],
            "seo": [],
            "security": [],
            "validation": [],
            "accessibility": [],
        })
    '''

    # inserisco l'elemento nella categoria corretta
    element = {
        "tool": report.tool,
        "stats": report.stats,
        "notes": report.notes,
        "documents": report.documents,
        "timestamp": str(datetime.now())
    }

    print(table.all()[0][report.type])

    #table.update(addReportToCat(element), where(report.type).exists())

def addReportToCat(item):
    def transform(doc):
        print(doc)

    return transform

# Function to remove a report in the database
def removeReport(test_name: str, test_id: int):
    db = TinyDB(db_path)

    # check if the given table exists
    if not test_name in db.tables():
        return "Table with the given name doesn't exist."
    table = db.table(test_name)

    if table.contains(doc_id=test_id):
        table.remove(doc_ids=[test_id])
        return "Report removed."
    

    return "Report with the given id doesn't exist."
    

def getScores(test_name: str):
    db = TinyDB(db_path)

    # check if the given table exists
    if not test_name in db.tables():
        return "Table with the given name doesn't exist."
    table = db.table(test_name)
    reports_db = Query()

    score_docs = table.search((reports_db.stats.score.exists()) & (reports_db.stats.score != None))

    score_list = []

if __name__ == "__main__":
    setupDB()

