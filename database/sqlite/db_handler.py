from .models import *
from sqlalchemy.orm import Session
from sqlalchemy import select

from pydantic import BaseModel
from datetime import datetime

'''
    GUARDA: 
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_related_objects.htm
    https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#adding-relationships-to-mapped-classes-after-declaration

    TODO: sistemare input rispetto a relazioni (sono liste/attributo dell'instanza!)
        + impostare input da chiamata API come input della RUN (quindi con tutti i report dei tool messi insieme!)
'''


# model for the data received to insert into the database
# reports: list of report with 'type', 'tool', 'scores', 'notes', json_report'
class Item(BaseModel):
    url: str
    reports: list


# DA SISTEMARE!!!!
def insert_report(db: Session, item: Item):
    # Run model -> search if exists, and, if it doesn't, create a new one
    run_result = db.execute(select(Run).where(Run.url == item.url)).first()
    if run_result == None:
        run_record = Run(
            url=item.url,
        )
    else:
        run_record = run_result[0]

    # All reports with tool and scores
    for r in item.reports:
        # REPORT
        report_record = Report(
            notes=r['notes'],
            json_report=r['json_report'],
            timestamp=datetime.now(),
        )

        # SCORES
        if r['scores'] != None:
            for score_name, score in r['scores'].items():
                report_record.scores.append(Score(name=score_name, score=score))
        # TOOL
        # checks if tool already exists, and added if not
        tool_result = db.execute(select(Tool).where(Tool.name == r['tool'], Tool.type == r['type'])).first()
        if tool_result: report_record.tool = tool_result[0] 
        else: report_record.tool = Tool(name=r['tool'], type=r['type'])
            
        run_record.reports.append(report_record)

    # add new elements and commit changes
    db.add(run_record)
    db.commit()







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
