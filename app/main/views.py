from flask import Blueprint, render_template
from ..utils import get_posts_all, cut_content, get_bookmarks_all

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    data = get_posts_all()
    posts = []
    content_count = 1
    for post in data:
        short_content = {"poster_name": post["poster_name"].capitalize(), "poster_avatar": post["poster_avatar"],
                         "pic": post["pic"], "tag": post["tag"], "content": post["content"],
                         "views_count": post["views_count"], "likes_count": post["likes_count"], "pk": post["pk"],
                         "content_count": content_count, "short_content": cut_content(post["content"])}
        content_count += 1
        posts.append(short_content)
    bookmarks = get_bookmarks_all()
    bookmarks_count = 0
    for bookmark in bookmarks:
        bookmarks_count += 1
    return render_template("index.html", posts=posts, bookmarks_count=bookmarks_count)

