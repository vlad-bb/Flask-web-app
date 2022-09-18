def validation_lang(language):
    if language in ['ru', 'en', 'english', 'russian', 'англійська', 'русский', 'ua', 'україньска']:
        return language
    else:
        return None
