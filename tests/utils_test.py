from app.utils import get_posts_all, get_posts_by_user, get_post_by_pk, get_comments_by_post_id, search_for_posts

posts_keys = {"poster_name", "poster_avatar", "pic", "tag", "content", "views_count", "likes_count", "pk"}
comments_keys = {"post_id", "commenter_name", "comment", "pk"}


class TestUtils:

    def test_get_posts_all(self):
        posts = get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == posts_keys, "неверный список ключей"

    def test_get_posts_by_user(self):
        posts_by_user = get_posts_by_user("leo")
        assert posts_by_user[0]["poster_name"] == "leo", "возвращаются неправильные посты"
        assert set(posts_by_user[0].keys()) == posts_keys, "неверный список ключей"
        assert len(posts_by_user) != 0,  "нераспознана ошибка типа ValueError"

    def test_get_comments_by_post_id(self):
        comments_by_post_id = get_comments_by_post_id(1)
        for comment in comments_by_post_id:
            result = comment["post_id"]
        assert type(comments_by_post_id) == list, "возвращается не список"
        assert len(comments_by_post_id) > 0, "нераспознана ошибка типа ValueError"
        assert result == 1, "возвращаются неправильные комментарии"
        assert set(comments_by_post_id[0].keys()) == comments_keys, "неверный список ключей"

    def test_search_for_posts(self):
        search_by_query = search_for_posts("Квадратная")
        for post in search_by_query:
            result = post['content'].lower().split(" ")
        assert type(search_by_query) == list, "возвращается не список"
        assert len(search_by_query) > 0, "нераспознана ошибка типа ValueError"
        assert "Квадратная".lower() in result, "возвращаются неправильные посты"
        assert set(search_by_query[0].keys()) == posts_keys, "неверный список ключей"

    def test_get_post_by_pk(self):
        post = get_post_by_pk(1)
        assert post["pk"] == 1, "возвращается неправильный пост"
        assert set(post.keys()) == posts_keys, "неверный список ключей"
