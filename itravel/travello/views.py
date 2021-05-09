from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def homePage(request):
    dests = Destination.objects.all()
    context = {"dests":dests}
    return render(request,'itravel/index.html',context)

def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))
    context = {'dest':dest[0]}
    if dest:
        return render(request,'itravel/destination.html', context)
    
def view_profile(request):
    pass

def edit_profile(request):
    pass

def delete_profile(request):
    pass
