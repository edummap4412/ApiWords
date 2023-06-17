from sqlalchemy.orm import Session

from config.sql_alchemy.models import Words
from config.sql_alchemy.schemas import WordSchema


class WordsService(object):

    def save_words(self, db: Session, words: WordSchema):
        for word in words:
            _word = Words(word=word)
            db.add(_word)
            db.commit()
            db.refresh(_word)

