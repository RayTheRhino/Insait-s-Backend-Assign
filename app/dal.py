from app.models import AskRecord
from app import db

def save_record(question, response=None, error=None, status_code=None):
    try:
        new_rec = AskRecord(question=question, response=response, error=error, status_code=status_code)
        db.session.add(new_rec)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def get_all_records():
    return AskRecord.query.all()

def get_record_by_id(rec_id):
    return AskRecord.query.get(rec_id)
