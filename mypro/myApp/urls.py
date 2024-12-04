# news/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import article_list


urlpatterns = [
    path('', views.home, name='home'),
    path('article_list/', views.article_list, name='article_list'),
    path('home/', views.home, name='home'),  # Home page
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Article detail page
    path('like_article/<int:article_id>/', views.like_article, name='like_article'),
    path('world/', views.world, name='world'),
    path('politics/', views.politics, name='politics'),
    path('sports/', views.sports, name='sports'),
    path('entertainment/', views.entertainment, name='entertainment'),
     path('innovations/', views.innovations, name='innovations'),
      path('business/', views.business, name='business'),
    path('contact/', views.contact, name='contact'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
