from sqlalchemy import and_
from src import db
from src import models
from src.libs.file_service import move_user_audio, delete_user_audio


def get_audio_user(user_id):
    return db.session.query(models.Audio).filter(models.Audio.user_id == user_id).all()


def get_audio_user(pic_id, user_id):
    return db.session.query(models.Audio).filter(
        and_(models.Audio.user_id == user_id, models.Audio.id == pic_id)).one()


def upload_audio_for_user(user_id, file_path, description):
    # user = find_by_id(user_id)
    filename, size = move_user_audio(user_id, file_path)
    audio = models.Audio(description=description, user_id=user_id, path=filename, size=size)
    db.session.add(audio)
    db.session.commit()


def delete_audio(pic_id, user_id):
    audio = get_audio_user(pic_id, user_id)
    db.session.query(models.Audio).filter(
        and_(models.Audio.user_id == user_id, models.Audio.id == pic_id)).delete()
    delete_user_audio(audio.path)
    db.session.commit()
