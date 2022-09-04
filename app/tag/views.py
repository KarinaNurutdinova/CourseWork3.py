
from flask import Blueprint, render_template
from ..utils import get_post_by_tag, cut_content

tag_blueprint = Blueprint("tag_blueprint", __name__, template_folder="templates")


@tag_blueprint.route("/tag/<tag_name>")
def tag_page(tag_name):
    data = get_post_by_tag(tag_name)
    posts = []
    content_count = 1
    for post in data:
        short_content = {"poster_name": post["poster_name"].capitalize(), "poster_avatar": post["poster_avatar"],
                         "pic": post["pic"], "tag": post["tag"], "content": post["content"], "views_count": post["views_count"],
                         "likes_count": post["likes_count"], "pk": post["pk"], "content_count": content_count,
                         "short_content": cut_content(post["content"])}
        content_count += 1
        posts.append(short_content)
    return render_template('tag.html', posts=posts, tag_name=tag_name)
