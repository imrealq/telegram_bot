import sys

from sqlalchemy import (
    create_engine,
    Column, Integer, Text, String, DateTime, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from generic import DB_NAME

engine = create_engine(f'sqlite:///{DB_NAME}.db')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class HackerNewsDateTime(Base):
    __tablename__ = 'hacker_news_date_time'

    id = Column(Integer, primary_key=True, autoincrement=True)
    as_of = Column(DateTime)


class HackerNewsTopStories(Base):
    __tablename__ = 'hacker_news_top_stories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    as_of_id = Column(Integer, ForeignKey('hacker_news_date_time.id'))
    story_id = Column(Integer)
    story_score = Column(Integer)
    story_title = Column(Text)
    story_url = Column(Text)
    story_type = Column(String)


def main():
    if sys.argv[-1] == 'create_database':
        Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()