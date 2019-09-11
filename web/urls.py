from django.urls import path

from . import views_index, views_html, views_api

urlpatterns = [
    path('', views_index.index, name='index'),
    path('api/html/article/detail', views_html.get_article_detail, name='get_article_detail'),
    path('api/html/feeds/all', views_html.get_all_feeds, name='get_all_feeds'),
    path('api/html/homepage/intro', views_html.get_homepage_intro, name='get_homepage_intro'),
    path('api/html/issues/all', views_html.get_all_issues, name='get_all_issues'),
    path('api/html/articles/list', views_html.get_articles_list, name='get_articles_list'),

    path('api/lastweek/articles', views_api.get_lastweek_articles, name='get_lastweek_articles'),
    path('api/actionlog/add', views_api.add_log_action, name='add_log_action'),
    path('api/message/add', views_api.leave_a_message, name='leave_a_message'),
    path('api/feed/add', views_api.submit_a_feed, name='submit_a_feed'),
]
