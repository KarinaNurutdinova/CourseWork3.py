
from flask import Blueprint, render_template, request
from ..utils import search_for_posts, cut_content

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/search/", methods=['GET'])
def search_page():
    search_key = request.args.get('s', '')
    search_result = search_for_posts(search_key)
    posts = []
    posts_count = 0
    for post in search_result:
        posts_count += 1
        short_content = {"poster_name": post["poster_name"].capitalize(), "poster_avatar": post["poster_avatar"],
                         "pic": post["pic"], "tag": post["tag"], "content": post["content"], "views_count": post["views_count"],
                         "likes_count": post["likes_count"], "pk": post["pk"],
                         "short_content": cut_content(post["content"])}
        posts.append(short_content)
    return render_template('search.html', posts=posts, posts_count=posts_count, search_key=f'#{search_key}')

