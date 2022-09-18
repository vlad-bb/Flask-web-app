from gtts import gTTS
import pdfplumber
from pathlib import Path
from src.libs.file_service import move_user_mp3

from python_play.player import play_it


"""
Launch convector PDF to MP3
"""


def pdf_to_mp3(file_br, user_id, language='ru'):
    file = Path(file_br)
    if file.is_file() and file.suffix == '.pdf':
        with pdfplumber.PDF(open(file=file, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        # print(f'Start convert PDF to MP3\nPlease wait...')
        text = ''.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = file.stem
        # mp3_folder = Path('pdf-mp3/mp3')
        path = move_user_mp3(user_id, file)
        my_audio.save(f'{path/file_name}.mp3')
        # print(f'{file_name}.mp3 saved')
    #     if play == 'y':
    #         play_it(f'{(mp3_folder/file_name).resolve()}.mp3')
    #     else:
    #         print('End program')
    #
    # else:
    #     print(f'{file} not exist')

#
# def run_play(file):
#     file = Path(file)
#     if file.is_file() and file.suffix == '.mp3':
#         play_it(file_path)
#         file_name = file.stem
#         print(f'MP3 was played {file_name}')
#     else:
#         print(f'{file} not exist')


