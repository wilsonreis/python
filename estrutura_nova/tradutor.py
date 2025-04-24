import asyncio
import json
from googletrans import Translator
from gtts import gTTS
import os

async def translate_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            english_text = f.read()

        translator = Translator()
        translation = await translator.translate(english_text, dest='pt')
        translated_text = translation.text

        # Crie um arquivo de áudio com a tradução
        tts = gTTS(text=translated_text, lang='pt')
        tts.save('tradução.mp3')

        # Reproduza o arquivo de áudio
        os.system('start tradução.mp3')

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        print("Make sure the file is in the correct location and the path is accurate.")

    except (json.JSONDecodeError, TypeError):
        print("Error decoding JSON response or unexpected response format.")
        print("This could be due to:")
        print(" - A temporary issue with the Google Translate API.")
        print(" - API rate limits.")
        print(" - An invalid input.")
        print("Please try again later or check your input.")

async def main():
    file_path = 'english_text.txt'
    await translate_file(file_path)

asyncio.run(main())