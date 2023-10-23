from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('write/', views.post_create, name='post_create'), 
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'), 
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'), 
    path('<int:post_id>/', views.post_detail, name='post_detail'), 
    path('', views.post_list, name='post_list'),  # 가장 마지막에 빈 문자열 패턴을 추가
    path('comment/<int:post_id>/', views.comment, name='comment')
]


