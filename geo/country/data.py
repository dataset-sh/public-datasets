from dataset_sh.constants import DEFAULT_COLLECTION_NAME
import requests
import json

def create_collection():
    languages = requests.get('https://gist.githubusercontent.com/joshuabaker/d2775b5ada7d1601bcd7b31cb4081981/raw/fb71e8ff9d7d970899d690fe23351601c5b70f04/languages.json')
    codes = json.loads(languages.content)
    return codes


def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: create_collection()
    }