from django.urls import path
# index는 대문, blog는 게시판
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>',views.posting, name="posting"),
    path('portfolio/',views.portfolio,name="portfolio")
]
