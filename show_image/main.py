import logging
from flask import render_template, Blueprint, request

from functions import load_post

show_image_blueprint = Blueprint('show_image_blueprint', __name__, template_folder='templates')
logging.basicConfig(level=logging.INFO)


@show_image_blueprint.route('/')
def main_page():
    logging.info("Выполнен поиск")
    return render_template('index.html')


@show_image_blueprint.route('/search/')
def search_page():

    search_by = request.args['s']
    post = []
    for i in load_post():
        if search_by.lower() in i['content'].lower():
            post.append(i)
    return render_template('post_list.html', post=post, search_by=search_by)
