from flask import Blueprint, jsonify
from werkzeug.exceptions import abort
from ..utils import get_posts_all, get_post_by_pk

import logging

from config import DATA_PATH_POST, DATA_PATH_COMMENTS

post_main = DATA_PATH_POST
comments_main = DATA_PATH_COMMENTS

api_blueprint = Blueprint('api_blueprint', __name__)
api_logger = logging.getLogger("api_logger")

logging.basicConfig(filename="logs/api.log", level=logging.INFO)


@api_blueprint.route('/api', methods=['GET'])
def api_posts_hello():
    return 'Попроси у меня документацию'


@api_blueprint.route('/api/posts', methods=['GET'])
def api_posts_all():
    """Возвращает полный список постов в виде JSON-списка"""
    all_posts = get_posts_all()
    api_logger.info('Запрошены все посты')
    return jsonify([post for post in all_posts]), 200


@api_blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def api_post_single(pk):
    """Возвращает один пост в виде JSON-словаря"""
    post = get_post_by_pk(pk)

    if post is None:
        api_logger.debug('Обращение к несуществующему посту')
        abort(404)
    api_logger.info(f'Обращение к посту {pk}')
    return jsonify(post), 200


