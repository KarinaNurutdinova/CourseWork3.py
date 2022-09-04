from flask import Blueprint, render_template
from ..utils import get_posts_by_user, cut_content

users_blueprint = Blueprint("users_blueprint", __name__, template_folder="templates")


@users_blueprint.route("/users/<username>", methods=['GET'])
def user_page(username):
    data = get_posts_by_user(username)
    posts = []
    content_count = 1
    for post in data:
        short_content = {"poster_name": post["poster_name"].capitalize(), "poster_avatar": post["poster_avatar"],
                         "pic": post["pic"], "tag": post["tag"], "content": post["content"], "views_count": post["views_count"],
                         "likes_count": post["likes_count"], "pk": post["pk"], "content_count": content_count,
                         "short_content": cut_content(post["content"])}
        content_count += 1
        posts.append(short_content)
    return render_template("user-feed.html", posts=posts)
