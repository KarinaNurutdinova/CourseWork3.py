from flask import Flask
from app.main.views import main_blueprint
from app.posts.views import post_blueprint
from app.search.views import search_blueprint
from app.users.views import users_blueprint
from app.tag.views import tag_blueprint
from app.bookmarks.views import bookmarks_blueprint
from exceptions.exceptions import NonExistentPage
from app.api_endpoint.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def page_error_404(error):
    return f'Такой страницы не существует {error}', 404


@app.errorhandler(500)
def page_error_500(error):
    return f'На сервере произошла ошибка {error}', 500


@app.errorhandler(NonExistentPage)
def page_error_non_existent(error):
    return f'Ошибка, что-то с данными {error}', 500


if __name__ == "__main__":
    app.run(port=8000)

