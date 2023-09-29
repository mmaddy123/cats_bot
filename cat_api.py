from googletrans import Translator
import requests
import json


# def get_cat():
#     url = "https://cataas.com/cat"
#     response = requests.get(url)
#     with open('cat.jpeg', 'wb') as file:
#         file.write(response.content)


def get_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    cat_fact = response.json()
    return cat_fact["fact"]


def get_fact_ru():
    text = get_fact()
    translator = Translator()
    translation = translator.translate(text, dest='ru')
    return translation.text

