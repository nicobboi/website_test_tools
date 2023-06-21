import os
import sqlite3
from sqlite3 import Error
from databases import Database

from datetime import datetime
from pydantic import BaseModel

class Report(BaseModel):
    url: str
    type: str
    tool: str
    scores: dict | None
    notes: str | None
    json_report: dict | None


database = Database("sqlite+aiosqlite://./sqlite_db/app.db")


async def db_startup():
    await database.connect()

async def db_shutdown():
    await database.disconnect()



'''
# push the report data into the database
def insert_report(report: Report):
    try:
        conn = sqlite3.connect(os.path.dirname(__file__) + '/sqlite_db/app.db')
        print("[INFO]: Successful connection!")
        cur = conn.cursor()

        # check if TEST exists and, if it does, insert into the db
        cur.execute("SELECT url FROM tests WHERE url = ?", (report.url, ))
        res = cur.fetchone()
        if not res:
            cur.execute("INSERT INTO tests VALUES(?)", (report.url, ))
            print("[INFO]: New test inserted!")

        # insert the REPORT
        cur.execute("INSERT INTO reports (tool, score, score_weight, notes, timestamp, test_url) VALUES (?, ?, ?, ?, ?, ?)", 
                    (report.tool, report.score, report.score_weight, report.notes,
                    str(datetime.now()), report.url))
        print("[INFO]: Report inserted!")
        
        # insert, if exist, the documents
        if report.documents:
            for file, file_name in report.documents:
                # TODO: converti file in blob
                cur.execute("INSERT INTO documents (json_report, report_id) VALUES (?, ?, ?)",
                            (file, cur.lastrowid))
            print("[INFO]: All documents inserted!")
                
        conn.commit()

        print("[INFO]: Insertion terminated.")

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        else:
            print("Errore generico.")
'''
