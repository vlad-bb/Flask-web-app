from sqlalchemy import and_
from src import db
from src import models
from src.libs.file_service import move_user_audio, delete_user_audio
from pathlib import Path


def get_audios_user(user_id):
    return db.session.query(models.Audio).filter(models.Audio.user_id == user_id).all()


def get_audio_user(audio_id, user_id):
    return db.session.query(models.Audio).filter(
        and_(models.Audio.user_id == user_id, models.Audio.id == audio_id)).one()


def upload_audio_for_user(user_id, file_path: Path):
    # user = find_by_id(user_id)
    filename, size = move_user_audio(user_id, file_path)
    name = file_path.name
    audio = models.Audio(description=name, user_id=user_id, path=filename, size=size)
    db.session.add(audio)
    db.session.commit()


def delete_audio(audio_id, user_id):
    audio = get_audio_user(audio_id, user_id)
    db.session.query(models.Audio).filter(
        and_(models.Audio.user_id == user_id, models.Audio.id == audio_id)).delete()
    delete_user_audio(audio.path)
    db.session.commit()


def update_audio(pic_id, user_id, description):
    picture = get_audio_user(pic_id, user_id)
    picture.description = description
    db.session.commit()
