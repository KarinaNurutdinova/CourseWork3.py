import json
from exceptions.exceptions import NonExistentPage
from flask import request


def get_posts_all():
    """Возвращает посты"""
    with open("./data/posts.json", "r", encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    user_name = user_name.lower()
    users_posts = []
    posts = get_posts_all()
    for post in posts:
        if post["poster_name"] == user_name:
            users_posts.append(post)
    if len(users_posts) == 0:
        raise ValueError("У пользователя нет постов")
    return users_posts


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста"""
    with open("./data/comments.json", "r", encoding="utf-8") as file:
        comments = json.load(file)
    posts_comments = []
    for comment in comments:
        if comment["post_id"] == int(post_id):
            posts_comments.append(comment)

    return posts_comments


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    query = query.lower()
    search_result = []
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        posts_query.append(post["content"].lower())
        if query in post["content"].lower():
            search_result.append(post)
    return search_result
    if query not in posts_query:
        raise NonExistentPage("Посты по ключевому слову не найдены")


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    posts_pk = []
    for post in posts:
        posts_pk.append(post["pk"])
        if post["pk"] == pk:
            return post
    if pk not in posts:
        raise NonExistentPage("Нет поста с таким идентификатором")


def cut_content(text):
    """Обрезает текст до 50 символов"""
    cut_text = []
    simbols_count = 0
    for simbols in text:
        if simbols_count <= 50:
            cut_text.append(simbols)
            simbols_count += 1
    cut_text.append("...")
    cut_text = "".join(cut_text)
    return cut_text


def get_post_by_tag(tag_name):
    tag = tag_name.lower()
    tag_posts = []
    posts = get_posts_all()
    for post in posts:
        if post["tag"] == tag:
            tag_posts.append(post)
    if len(tag_posts) == 0:
        raise ValueError("Нет постов")
    return tag_posts


def get_bookmarks_all():
    """Возвращает закладки"""
    with open("./data/bookmarks.json", "r", encoding='utf-8') as file:
        bookmarks = json.load(file)
    return bookmarks


def add_bookmark(post_id):
    """Добавляет в закладки"""
    bookmark = get_post_by_pk(post_id)
    with open("./data/bookmarks.json", "r", encoding='utf-8') as file:
        bookmarks = json.load(file)
    with open("./data/bookmarks.json", "w", encoding='utf-8') as file:
        json.dump(bookmarks, file)


def remove_bookmark(post_id):
    """Удаляет закладки"""
    with open("./data/bookmarks.json", "r", encoding='utf-8') as file:
        bookmarks = json.load(file)
        bookmarks_num = 0
        for bookmark in bookmarks:
            if bookmark["pk"] == post_id:
                bookmarks_num += 1
                del bookmarks[bookmarks_num]
    with open("./data/bookmarks.json", "w", encoding='utf-8') as file:
        json.dump(bookmarks, file)
