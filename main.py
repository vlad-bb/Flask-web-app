from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint
from tqdm import tqdm
from python_play.player import play_it


def pdf_to_mp3(file_br, play, language='en'):
    file = Path(file_br)
    if file.is_file() and file.suffix == '.pdf':
        with pdfplumber.PDF(open(file=file, mode='rb')) as pdf:
            pages = [page.extract_text() for page in tqdm(pdf.pages)]
        print(f'Start convert PDF to MP3\nPlease wait...')
        text = ''.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = file.stem
        mp3_folder = Path('pdf-mp3/mp3')
        my_audio.save(f'{mp3_folder/file_name}.mp3')
        print(f'{file_name}.mp3 saved')
        if play == 'y':
            play_it(f'{(mp3_folder/file_name).resolve()}.mp3')
        else:
            print('End program')

    else:
        print(f'{file} not exist')


def run_play(file):
    file = Path(file)
    if file.is_file() and file.suffix == '.mp3':
        play_it(file_path)
        file_name = file.stem
        print(f'MP3 was played {file_name}')
    else:
        print(f'{file} not exist')


if __name__ == '__main__':
    tprint('PDF>>TO>>MP3')
    # file_path = input("Choose PDF file: ")
    # lang = input("Choose language 'en' or 'ru': ")
    # auto_play = input('Start playing after convert to mp3?(y/n): ')
    # pdf_to_mp3(file_path, auto_play, lang)
    file_path = input("Choose MP3 file: ")
    run_play(file_path)