from .models import *
from sqlalchemy.orm import Session
from sqlalchemy import select

from pydantic import BaseModel
from datetime import datetime

'''
    GUARDA: 
    https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_working_with_related_objects.htm
    https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#adding-relationships-to-mapped-classes-after-declaration
'''


# model for the data received to insert into the database
# reports: list of report with 'type', 'tool', 'scores', 'notes', json_report'
class Item(BaseModel):
    url: str
    reports: list


# push a set of reports into the database
def insert_reports(db: Session, item: Item):
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


# delete a report by his ID
def delete_item(db: Session, report_id, run_id):
    if report_id != None:
        db.delete(db.get(Report, report_id))
    if run_id != None:
        db.delete(db.get(Run, run_id))
    db.commit()


# return all scores form all report of a specified run (between two datetime if are given)
def get_scores(db: Session, url, date_start, date_end):
    # Selects tools name and scores info of all the reports of the specified run
    query = select(Tool.name, Tool.type, Score.name, Score.score) \
        .join(Report, Tool.reports) \
        .join(Run) \
        .where(Run.url == url, Report.id == Score.report_id)
    
    # if specified, filter by datetime
    if date_start != None and date_end != None:
        query = query.filter(Report.timestamp > date_start, Report.timestamp < date_end)

    # execute the query
    result = db.execute(query)

    # return a list of dict, that will be implicit converted as JSON after
    return [r._asdict() for r in result]

    

