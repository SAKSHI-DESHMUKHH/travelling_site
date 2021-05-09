from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from .forms import DestinationForm,operationsForm
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer

def homePage(request):
    dests = Destination.objects.all()
    context = {"dests":dests}
    return render(request,'itravel/index.html',context)

def dest_details(request,dest_id):
    dest=list(Destination.objects.filter(id=dest_id))
    context = {"dest":dest[0]}
    if dest:
        return render(request,'itravel/destination.html', context)

def dest_add(request):
    if request.method=='POST':
        form = DestinationForm(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request,'Error while creating Destination')
    return render(request,'itravel/destinationform.html',{'form':DestinationForm()})

# @api_view(['GET'])
# def apiOverview(request):
#     api_urls={

#     }

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/destination_lists/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)
    
@api_view(['GET'])
def get_all_destinations(request):
    dests=Destination.objects.all()
    serializer=DestinationSerializer(dests,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def destinations_detail(request,pk):
    dests=Destination.objects.get(id=pk)
    serializer=DestinationSerializer(dests,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def destinations_create(request):
    serializer=DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def destinations_update(request,pk):
    dests=Destination.objects.get(id=pk)
    serializer = DestinationSerializer(instance=dests,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def destinations_delete(request,pk):
    dests=Destination.objects.get(id=pk)
    dests.delete()
    return Response("Item successfully deleted")

def view_profile(request):
    pass

def update_profile(request,pk):
    dests=Destination.objects.get(id=pk)
    form = operationsForm(instance=dests)
    if request.method == "POST":
        # print(request.POST)
        form = operationsForm(request.POST,instance=dests)
        if form.is_valid():
            form.save()
        return redirect('/')        
    context={'form':form}
    return render(request, 'itravel/destination_form.html',context)

def delete_profile(request,pk):
    dests = Destination.objects.get(id=pk)
    if request.method == "POST":
        dests.delete()
        return redirect('/') 
    context={'item':dests}
    return render(request, 'itravel/delete.html',context)
