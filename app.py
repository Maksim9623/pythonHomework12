import logging
from flask import Flask, request, render_template, send_from_directory

from show_image.main import show_image_blueprint
from load.load import load_blueprint


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

# Регистрируем первый блюпринт
app.register_blueprint(show_image_blueprint)
# И второй тоже регистрируем
app.register_blueprint(load_blueprint)


# Вьюшка, для доступа пользователей к папке static
@app.route("/uploads/images/<path:path>")
def static_dir(path):
    logging.info("Загруженный файл - не картинка")
    return send_from_directory("uploads/images", path)



if __name__ == "__main__":
    app.run(debug=False)

