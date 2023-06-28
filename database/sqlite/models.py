from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.types import DateTime, JSON

from sqlalchemy.orm import relationship
from .database import Base

# Run 1:N Report
class Run(Base):
    __tablename__ = "runs"

    id          = Column(Integer, primary_key=True, index=True)
    url         = Column(String, nullable=False)

    reports     = relationship("Report", back_populates="run")

# Report 1:N Score (one report has more scores, one score is in one report)
# Report N:1 Tool
# Report N:1 Run
class Report(Base):
    __tablename__ = "reports"

    id          = Column(Integer, primary_key=True, index=True)
    tool_id     = Column(Integer, ForeignKey("tools.id", onupdate="CASCADE", ondelete="CASCADE"))
    notes       = Column(Text, nullable=True)
    json_report = Column(JSON, nullable=True)
    run_id      = Column(Integer, ForeignKey("runs.id", onupdate="CASCADE", ondelete="CASCADE"))
    timestamp   = Column(DateTime, nullable=False)
    
    tool        = relationship("Tool", back_populates="reports")
    scores      = relationship("Score", back_populates="report")
    run         = relationship("Run", back_populates="reports")


# Tool 1:N Report
class Tool(Base):
    __tablename__ = "tools"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    type        = Column(String, nullable=False)

    reports     = relationship("Report", back_populates="tool")

    UniqueConstraint(name)

# Score N:1 Report
class Score(Base):
    __tablename__ = "scores"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String, nullable=False)
    score       = Column(Integer, nullable=False)
    report_id   = Column(Integer, ForeignKey("reports.id", onupdate="CASCADE", ondelete="CASCADE"))

    report      = relationship("Report", back_populates="scores")