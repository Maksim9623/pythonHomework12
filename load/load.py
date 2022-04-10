import logging
from flask import render_template, Blueprint, request

from functions import load_post, upload_image

load_blueprint = Blueprint('load_blueprint', __name__, url_prefix='/post', static_folder='static', template_folder='templates')
logging.basicConfig(level=logging.ERROR)


@load_blueprint.route('/form/')
def form_page():
    return render_template('post_form.html')


@load_blueprint.route('/upload/', methods=["POST"])
def upload_page():
    logging.error("Ошибка при загрузке файла")
    try:
        ALLOWED_EXTENSIONS = ['png', 'jpg', 'bmp', 'gif']
        picture = request.files.get('picture')
        filename = picture.filename
        content = request.values['content']
        post = load_post()
        post.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        extension = filename.split('.')[-1]
        upload_image(post)
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f'./uploads/images/{filename}')
        else:
            return "Тип файла не поддерживается, повторите процесс снова!"
    except ValueError:
        return "<h2> Ошибка при загрузки файла <br> <a href="/">Назад</a> </h2>"
    except FileNotFoundError:
        return "<h2> Файл не найден <br> <a href="/">Назад</a> </h2>"

    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)

