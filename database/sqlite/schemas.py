from datetime import datetime
from pydantic import BaseModel

class Run(BaseModel):
    id:             int
    url:            str
    timestamp:      datetime
    class Config: orm_mode = True


class Tool(BaseModel):
    id:             int
    name:           str
    type:           str
    class Config: orm_mode = True


class Report(BaseModel):
    id:             int
    notes:          str | None
    json_report:    dict | None
    tool_id:        int
    run_id:         int
    class Config: orm_mode = True


class Score(BaseModel):
    id:             int
    name:           str
    score:          int
    report_id:      int
    class Config: orm_mode = True
