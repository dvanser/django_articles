from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('tags/<slug:tag_slug>/', views.TagIndexView.as_view(), name='articles_by_tag'),
]