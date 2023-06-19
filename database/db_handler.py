from tinydb import TinyDB
from datetime import datetime
import os

def insertTest(test_name, URL, test_type, tool_name, stats, documents, notes):
    db_path = os.path.dirname(__file__) + "/reports_db.json"

    db = TinyDB(db_path, indent=4, separators=(',', ': '))
    table = db.table(test_name)

    element = {
        "url": URL,
        "type": test_type,
        "tool": tool_name,
        "stats": stats,
        "notes": notes,
        "documents": documents,
        "timestamp": str(datetime.now())
    }

    table.insert(element)

    print(tool_name + " report inserito nel DB!")


