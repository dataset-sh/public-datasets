from dataset_sh.constants import DEFAULT_COLLECTION_NAME


def create_data_dict():
    return {
        DEFAULT_COLLECTION_NAME: [
            {'language': 'en', 'value': 'Hello World!'},
            {'language': 'fr', 'value': "Bonjour le monde!"},
            {'language': 'es', 'value': "¡Hola Mundo!"},
            {'language': 'de', 'value': "Hallo Welt!"},
            {'language': 'it', 'value': "Ciao Mondo!"},
            {'language': 'pt', 'value': "Olá Mundo!"},
            {'language': 'zh', 'value': "你好，世界！"},
            {'language': 'ja', 'value': "こんにちは世界！"},
            {'language': 'hi', 'value': "नमस्ते दुनिया!"},
            {'language': 'ar', 'value': "مرحبا بالعالم!"},
            {'language': 'ru', 'value': "Привет, мир!"},
            {'language': 'ko', 'value': "안녕하세요 세계!"},
        ]
    }