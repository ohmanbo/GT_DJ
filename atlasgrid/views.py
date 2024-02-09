from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import account, grid, HelloWorld
from rest_framework import viewsets
from django.urls import reverse


class AtlasGridInfo( viewsets.ModelViewSet ):
    queryset = grid.objects.all()
    #serializer_class = AtlasGridInfoSerializer


# Create your views here.
def view(request):
    userlist = account.objects.all()
    context = {'userlist': userlist}
    
    if request.method == 'POST':
        
        temp = request.POST.get('monitor_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('monitor'))
    
    else:
        hello_world_list = HelloWorld.objects.all()
        hello_world_list_reversed = hello_world_list[::-1]
        return render(request, 'atlasgrid/monitor.html', context={'monitor_output': hello_world_list_reversed})