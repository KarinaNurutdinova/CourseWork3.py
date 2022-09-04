import pytest
from run import app

posts_keys = {"poster_name", "poster_avatar", "pic", "tag", "content", "views_count", "likes_count", "pk"}


class TestApi:

    @pytest.fixture
    def test_api_posts_hello(self):
        assert "Попроси у меня документацию", "Запрос документации не работает"

    def test_api_posts_all(self):
        response = app.test_client().get('/api/posts')
        assert type(response.json) == list, "возвращается не список"
        assert len(response.json) > 0, "возвращается пустой список"
        assert set(response.json[0].keys()) == posts_keys, "неверный список ключей"

    def test_api_post_single(self):
        response = app.test_client().get('/api/posts/1')
        post = response.json
        assert type(post) == dict, "возвращается не словарь"
        assert len(post) > 0, "возвращается пустой словарь"
        assert set(post.keys()) == posts_keys, "неверный список ключей"
