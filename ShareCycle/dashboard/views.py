from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import User, Items

# Create your views here.

def index(request):
        return render(request, 'welcome.html')


@login_required
def dashboard(request):
    user = request.user
    inds = User.objects.filter(user = user)
    itms = Items.objects.all()
    context ={
        'user':user,
        'inds':inds,
        'itms':itms
    }
#     ind_list = []
#     itm_list = []
#     for ind in inds:
#         contact = ind.user_contact
#         ind_list.append(contact)
#     print(ind_list)

#     for itm in itms:
#         item_id = itm.id
#         itm_list.append(item_id)

#     print(itm_list)    

    return render(request, 'dashboard/home.html', context)

def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_category = request.POST.get('item_category')
        item_pic = request.POST.get('item_pic')
        item_exp_date = request.POST.get('item_exp_date')
        item_collect_before = request.POST.get('item_collect_before')
        item_description = request.POST.get('item_description')
        itemm = Items(
            item_name=item_name,
            item_category = item_category,
            item_pic = item_pic,
            item_exp_date = item_exp_date,
            item_collect_before = item_collect_before,
            item_description = item_description
        )
        itemm.save()

        return redirect('dashboard')


    return render(request, 'dashboard/add_item.html')