from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

from configs.database_config import base as Base

class ParsingLog(Base):
    """
        Parsing Logs model
    """
    __tablename__ = 'parsing_logs'

    id = Column(Integer, primary_key=True, index=True)

    start_time = Column(DateTime, server_default=func.now())
    end_time = Column(DateTime, server_default=func.now())
    jobs_found = Column(Integer, default=0, nullable=True)
    errors = Column(Integer, default=0, nullable=True)

    account_id = Column(Integer, ForeignKey('accounts.id'))
    account = relationship('Account', back_populates='parsing_logs', foreign_keys=[account_id])

    link_list_id = Column(Integer, ForeignKey('link_lists.id'))
    link_list = relationship('LinkList', back_populates='parsing_logs', foreign_keys=[link_list_id])

    def __repr__(self) -> str:
        return (f'<ParsingLog(id={self.id}, account_id={self.account_id}, '
                f'link_list_id={self.link_list_id}, start_time={self.start_time}, '
                f'end_time={self.end_time}, jobs_found={self.jobs_found}, errors={self.errors})>')

    def __str__(self) -> str:
        return (f'ParsingLog(id={self.id}, account_id={self.account_id}, '
                f'link_list_id={self.link_list_id}, start_time={self.start_time}, '
                f'end_time={self.end_time}, jobs_found={self.jobs_found}, errors={self.errors})>')