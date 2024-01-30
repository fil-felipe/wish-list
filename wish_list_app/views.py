from django.shortcuts import render, get_object_or_404
from .models import PresentUser, PresentList
from .forms import FindMetaForm
from .get_meta.main import find_meta

def view_wish_list_user(request):
    """Return website with list of all user which have wish lists"""
    users = PresentUser.objects.all()
    return render(request,
            'wish_list_app/wish_list_users.html',
                  {'users': users}
            )

def view_wish_list(request, list_user_id):
    """Return website with list of all wish list for specific user"""
    list_user_object = get_object_or_404(PresentUser, id=list_user_id)
    user_wish_lists = list_user_object.present_lists.all()
    return render(request,
           'wish_list_app/wish_lists.html',
           {'user_wish_lists': user_wish_lists}
           )

def view_wish_list_items(request):
    """Return website with list of all wish list for specific user"""
    pass
def find_meta_info(request):
    meta_info = None
    if request.method == 'POST':
        form = FindMetaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            meta_info = find_meta(cd.get("html"))
    else:
        form = FindMetaForm()
    return render(request,
                  'wish_list_app/add_item/find_meta.html',
                  {'form': form, 'meta_info': meta_info}
                  )
