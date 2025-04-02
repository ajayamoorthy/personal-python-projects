from translate import Translator

available_languages = ["ja", "ko", "pt", "es", "ta"]

# asks user to pick a language to translate into and a txt file to translate
def whichLanguage():
    while True:
        print(f"currently supported ISO 639 codes: {available_languages}")
        lang = input("Pick a language to translate into (use an ISO 639 code): ")
        if lang in available_languages:
            translator = Translator(to_lang=lang)
            break
        else:
            print("Not a valid language code. Select from the options provided.")
    return translator

# creates a new file containing translated text
def translate(translator):
    fileRequest = input("What .txt file would you like translated (ex. introduction)?: ")
    print("Attempting to translate...")

    with open('%s.txt' % fileRequest, mode='r') as toTranslate:
        file_lines = toTranslate.readlines()
        with open('translated_%s.txt' % fileRequest, mode="w", encoding='utf-8') as translatedFile:
            for line in file_lines:
                translatedFile.write(translator.translate(line) + "\n")

    print(f"Translated!")

translator = whichLanguage()
translate(translator)
