from django.urls import path
from . import views

app_name = 'wish_list_app'
urlpatterns = [
    path('', views.view_wish_list_user, name='list_users'),
    path('<int:list_user_id>/', views.view_wish_list, name='user_lists'),
    path('find_meta', views.find_meta_info, name='find_meta'),
]