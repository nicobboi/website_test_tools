from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.types import DateTime, JSON

from sqlalchemy.orm import relationship
from .database import Base

# Run N:1 Report
class Run(Base):
    __tablename__ = "runs"

    id          = Column(Integer, primary_key=True, index=True)
    url         = Column(String, nullable=False)
    timestamp   = Column(DateTime, nullable=False)

    reports     = relationship("Report", back_populates="run")

# Report N:1 Score (one report has more scores, one score is in one report)
# Report N:1 Tool
# Report 1:N Run
class Report(Base):
    __tablename__ = "reports"

    id          = Column(Integer, primary_key=True, index=True)
    notes       = Column(Text, nullable=True)
    json_report = Column(JSON, nullable=True)
    run_id      = Column(Integer, ForeignKey("runs.id", onupdate="CASCADE", ondelete="CASCADE"))
    
    scores      = relationship("Score", back_populates="report")
    tools       = relationship("Tool", back_populates="report")
    run         = relationship("Run", back_populates="reports")


# Tool 1:N Report
class Tool(Base):
    __tablename__ = "tools"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False, unique=True)
    type        = Column(String, nullable=False)
    tool_id     = Column(Integer, ForeignKey("tools.id"), onupdate="CASCADE", ondelete="CASCADE")

    reports     = relationship("Report", back_populates="tools")

# Score 1:N Report
class Score(Base):
    __tablename__ = "scores"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    score       = Column(Integer, nullable=False)
    report_id   = Column(Integer, ForeignKey("reports.id", onupdate="CASCADE", ondelete="CASCADE"))

    report      = relationship("Report", back_populates="scores")