import os
import sqlite3
from sqlite3 import Error
from datetime import datetime
from pydantic import BaseModel

class Report(BaseModel):
    url: str
    type: str
    tool: str
    stats: dict | None
    notes: dict | None
    documents: dict | None

def insert_report(report: Report):
    try:
        conn = sqlite3.connect('/sqlite_db/app.db')
        print("[INFO]: Successful connesction!")
        cur = conn.cursor()

        sql_insert_query = '''
        INSERT INTO 
        '''

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        else:
            print("Errore generico.")
