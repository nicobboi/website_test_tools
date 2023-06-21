import models
from sqlalchemy.orm import Session

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
# TODO: deve diventare input della RUN (output tool messi tutti insieme)
class Report(BaseModel):
    url: str
    type: str
    tool: str
    scores: dict | None
    notes: str | None
    json_report: dict | None


# DA SISTEMARE!!!!
def insert_report(db: Session, report: Report):
    run_record = models.Run(
        urk=report.url,
        timestamp=datetime.now(),
    )

    report_record = models.Report(
        notes=report.notes,
        json_report=report.json_report,
    )

    report_record.tools += [
        models.Tool(
            name=report.tool,
            type=report.type
        )
    ]


    for score_name, score in report.scores:
        score_record = models.Tool(
            name=score_name,
            score=score
        )






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
