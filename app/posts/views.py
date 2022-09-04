from flask import Blueprint, render_template
from ..utils import get_comments_by_post_id, get_post_by_pk

post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates")


@post_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    post = get_post_by_pk(post_id)
    posts_comments = get_comments_by_post_id(post_id)
    comment_count = 0
    for comment in posts_comments:
        comment_count += 1
    if comment_count == 0:
        comment_count = "Пока нет"
    return render_template("post.html", post=post, comment_count=comment_count, posts_comments=posts_comments)
