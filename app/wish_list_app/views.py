from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import GiftUser, GiftList, Gift
from .forms import FindMetaForm, ReserveGift
from .get_meta.main import find_meta


def view_wish_list_user(request):
    """Return website with list of all user which have wish lists"""
    users = GiftUser.objects.all()
    return render(request, "wish_list_app/wish_list_users.html", {"users": users})


def view_wish_list_items(request, user, list_name):
    """Return website with list of all wish list for specific user"""
    gift_list_object = get_object_or_404(GiftList, list_user__slug=user, slug=list_name)
    gift_list = gift_list_object.gift_item.filter(reserved=False)
    return render(request, "wish_list_app/gift_list.html", {"gift_list": gift_list})


def view_wish_list(request, user):
    """Return website with list of all wish list for specific user"""
    list_user_object = get_object_or_404(GiftUser, slug=user)
    user_wish_lists = list_user_object.gift_lists.all()
    list_number = user_wish_lists.count()
    print(list_number)
    if list_number == 1:
        return redirect(user_wish_lists[0].get_absolute_url())
    return render(request, "wish_list_app/wish_lists.html", {"user_wish_lists": user_wish_lists})


def reserve_gift(request, user, list_name, gift):
    """Return website with page for gift reservation"""
    gift_object = get_object_or_404(
        Gift, gift_list__slug=list_name, gift_list__list_user__slug=user, slug=gift, reserved=False
    )

    if request.method == "POST":
        form = ReserveGift(data=request.POST, instance=gift_object)
        if form.is_valid:
            reservation = form.save(commit=False)
            reservation.reserved = True
            reservation.reserved_time = datetime.now()
            reservation.save()
            return redirect(gift_object.get_absolute_url())
    else:
        form = ReserveGift()

    return render(request, "wish_list_app/reserve_gift.html", {"gift": gift_object, "form": form})


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
