from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
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