import json

POST_PATH = "posts.json"


# Функция чтение файлов из JSON
def load_post():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        post = json.load(file)
        return post


# Функция запись файлов в JSON
def upload_image(post):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(post, file, ensure_ascii=False, indent=4)

