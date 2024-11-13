from django.urls import path
from . import views

app_name = "wish_list_app"
urlpatterns = [
    path("wish_lists", views.view_all_wish_lists, name="all_wish_lists"),
    path("<username>/", views.view_wish_list, name="user_lists"),
    path("child_register", views.add_child_user, name="child_register"),
    path("child_register_done/<username>", views.child_register_done, name="child_register_done"),
    path("add_list", views.add_wish_list, name="add_wish_list"),
    path("add_list/<username>", views.add_wish_list, name="add_wish_list_user"),
    path("<username>/<slug:list_name>/", views.view_wish_list_gifts, name="gift_lists"),
    path("add_gift", views.add_gift, name="add_gift"),
    path("add_gift/<slug:list_name>", views.add_gift, name="add_gift_list"),
    path("reserved", views.reserve_gift, name="reserve_gift"),
    path("find_meta", views.find_meta_info, name="find_meta"),
    path("<username>/<slug:list_name>/<slug:gift_slug>/edit/", 
         views.edit_gift, 
         name="edit_gift"),
    path("delete_gift/<int:gift_id>", views.delete_gift, 
         name="delete_gift")
]

