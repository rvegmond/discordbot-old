#!/usr/bin/env python


from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, DateTime

from datetime import datetime
from . import Base


class WSEntry(Base):
    __tablename__ = "wsentry"
    EntryId = Column(Integer, primary_key=True)
    UserId = Column(Integer, ForeignKey("user.UserId"))
    EntryType = Column(String)
    Remark = Column(String)
    EntryTime = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    Active = Column(Boolean, default=True)

    def __repr__(self):
        return (
            f"<WSEntry(EntryId={self.EntryId},"
            f"UserId={self.UserId},"
            f"EntryType={self.Remark},"
            f"Remark={self.Remark},"
            f"EntryTime={self.EntryTime},"
            f"Active={self.Active})>"
        )
