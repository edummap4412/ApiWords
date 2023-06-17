from sqlalchemy import Column, Integer, String
from config.sql_alchemy.config_sql_alchemy import Base


class Words(Base):
    __tablename__ = 'collected_words'

    id = Column(Integer, primary_key=True)
    word = Column(String)

