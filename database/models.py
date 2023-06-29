from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.types import DateTime, JSON

from sqlalchemy.orm import relationship
from database import Base

# Site 1:N Report
class Site(Base):
    __tablename__ = "sites"

    id          = Column(Integer, primary_key=True, index=True)
    url         = Column(String, nullable=False)

    reports     = relationship("Report", back_populates="site", cascade="all, delete, delete-orphan")

# Report 1:N Score (one report has more scores, one score is in one report)
# Report N:1 Tool
# Report N:1 Site
class Report(Base):
    __tablename__ = "reports"

    id          = Column(Integer, primary_key=True, index=True)
    tool_id     = Column(Integer, ForeignKey("tools.id", ondelete="NO ACTION"))
    notes       = Column(Text, nullable=True)
    json_report = Column(JSON, nullable=True)
    site_id      = Column(Integer, ForeignKey("sites.id", ondelete="CASCADE"))
    timestamp   = Column(DateTime, nullable=False)
    
    tool        = relationship("Tool", back_populates="reports")
    scores      = relationship("Score", back_populates="report", cascade="all, delete, delete-orphan")
    site         = relationship("Site", back_populates="reports")


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
    report_id   = Column(Integer, ForeignKey("reports.id", ondelete="CASCADE"))

    report      = relationship("Report", back_populates="scores")