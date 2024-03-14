from django.urls import path
from . import views

app_name = 'wish_list_app'
urlpatterns = [
    path('', views.view_wish_list_user, name='list_users'),
    path('<slug:user>/', views.view_wish_list, name='user_lists'),
    path('<slug:user>/<slug:list_name>/', views.view_wish_list_items, name='gift_lists'),
    path('reserve/<slug:user>/<slug:list_name>/<slug:gift>/', views.reserve_gift, name='reserve_gift'),
    path('find_meta', views.find_meta_info, name='find_meta'),
]