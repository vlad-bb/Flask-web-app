from gtts import gTTS
import pdfplumber
from pathlib import Path
from src.repository.audios import upload_audio_for_user



"""
Launch convector PDF to MP3
"""


def pdf_to_mp3(file, user_id, language='ru'):
    if file.is_file() and file.suffix == '.pdf':
        with pdfplumber.PDF(open(file=file, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = str(file)[:-3] + '.mp3'
        my_audio.save(file_name)
        upload_audio_for_user(user_id, Path(file_name), file_name)
        # path, size = move_user_audio(user_id, file)


