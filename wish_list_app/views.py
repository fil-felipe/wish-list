from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.text import slugify


from .models import Gift, WishList
from .forms import AddChildUser, AddWishList, AddWishListUser, AddGift, AddGiftToList, FindMetaForm
from .get_meta.main import find_meta

@login_required
def add_child_user(request):
    # optional_parameter = ''
    form_object = AddChildUser

    if request.method == "POST":
        form = form_object(data=request.POST)
        if form.is_valid:
            new_child_user = form.save(commit=False)

            new_child_user.parent_user = request.user
            new_child_user.save()

            return redirect('wish_list_app:child_register_done', username=new_child_user.username)
    else:
        form = form_object()
    return render(request, "child_register/child_register.html", {"form": form})

@login_required
def child_register_done(request, username):
    return render(request, "child_register/child_register_done.html", {"username": username})

@login_required
def add_wish_list(request, username=None):
    # optional_parameter = ''
    list_user_object = None
    form_object = AddWishList
    if username is not None:
        list_user_object = get_object_or_404(User, username=username)
        form_object = AddWishListUser

    if request.method == "POST":
        form = form_object(data=request.POST)
        if form.is_valid:
            new_wish_list = form.save(commit=False)
            if username is not None:
                new_wish_list.list_user = list_user_object
            new_wish_list.list_creator = request.user
            new_wish_list.list_name = f"{new_wish_list.list_user.first_name} {new_wish_list.list_user.last_name} " \
                                      f"- {new_wish_list.list_name}"
            new_wish_list.slug = slugify(new_wish_list.list_name)
            new_wish_list.save()
            return redirect(new_wish_list.get_absolute_url())
    else:
        form = form_object()
    return render(request, "wish_list_app/wish_lists/add_wish_list.html", {"user": list_user_object, "form": form})

@login_required
def view_all_wish_lists(request):
    all_wish_lists = WishList.objects.all()
    return render(request, "wish_list_app/wish_lists/all_wish_lists.html", {"all_wish_lists": all_wish_lists})
@login_required
def view_wish_list(request, username):
    list_user_object = get_object_or_404(User, username=username)
    user_wish_lists = list_user_object.gift_lists_user.all()
    list_number = user_wish_lists.count()
    return render(request, "wish_list_app/wish_lists/wish_lists.html", {"user": list_user_object, "user_wish_lists": user_wish_lists})

@login_required
def view_wish_list_gifts(request, username, list_name):
    gift_list_object = get_object_or_404(WishList, list_user__username=username, slug=list_name)
    gift_list = gift_list_object.gift_item.filter(reserved=False)
    return render(request, "wish_list_app/gifts/gift_list.html", {"gift_list": gift_list, "list_name": gift_list_object})

@login_required
def add_gift(request, list_name=None):
    form_object = AddGift
    list_object = None
    if list_name is not None:
        list_object = get_object_or_404(WishList, slug=list_name)
        form_object = AddGiftToList

    if request.method == "POST":
        form = form_object(request.POST)
        if form.is_valid:
            new_gift = form.save(commit=False)
            if list_name is not None:
                new_gift.gift_list = list_object
            else:
                list_object = new_gift.gift_list
            new_gift.slug = slugify(new_gift.title)
            new_gift.created_by = request.user
            new_gift.save()
            return redirect(list_object.get_absolute_url())
    else:
        form = form_object()

    return render(request, "wish_list_app/gifts/add_gift.html", {"list": list_object, "form": form})

@login_required
def reserve_gift(request, gift_id=None):
    if request.method == "POST":
        gift_id = request.POST.get('gift_id')
        gift_object = get_object_or_404(Gift, id=gift_id)
        gift_object.reserved = True
        gift_object.reserved_time = datetime.now()
        gift_object.reserved_user = request.user
        gift_object.save()
        return redirect(gift_object.get_absolute_url())

    return render(request, 'wish_list_app/reservation/failed_reserve.html')

@login_required
def find_meta_info(request):
    meta_info = None
    if request.method == "POST":
        form = FindMetaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            meta_info = find_meta(cd.get("html"))
    else:
        form = FindMetaForm()
    return render(request, "wish_list_app/add_item/find_meta.html", {"form": form, "meta_info": meta_info})

# TODO: get all gifts reserved by User and list them
# @login_required
# def view_reserved_gifts(request):
#     reserved_gift_list = None
#     if request.method == "POST":
#         form = FindMetaForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             meta_info = find_meta(cd.get("html"))
#     else:
#         form = FindMetaForm()
#     return render(request, "wish_list_app/reservation/view_reserved.html", {"form": form, "meta_info": meta_info})

@login_required
def edit_gift(request, username, list_name, gift_slug):
    gift = get_object_or_404(Gift, 
                            gift_list__list_user__username=username,
                            gift_list__slug=list_name,
                            slug=gift_slug)
    
    if request.method == "POST":
        form = AddGiftToList(instance=gift, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(gift.get_absolute_url())
    else:
        form = AddGiftToList(instance=gift)
    
    return render(request, 
                 "wish_list_app/gifts/edit_gift.html",
                 {"form": form, "gift": gift})

@login_required
def delete_gift(request, gift_id):
    gift = get_object_or_404(Gift, id=gift_id)

    if request.method == "POST":
        if request.user == gift.created_by or request.user == gift.gift_list.list_creator:
                list_url = gift.gift_list.get_absolute_url()
                gift.delete()
                return redirect(list_url)
    
    return render(request, 
                 "wish_list_app/gifts/delete_gift.html",
                 {"gift": gift})
