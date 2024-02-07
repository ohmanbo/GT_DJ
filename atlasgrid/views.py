from django.shortcuts import render
#from django.http.response import HttpResponse
from .models import account, grid, HelloWorld
from rest_framework import viewsets


class AtlasGridInfo( viewsets.ModelViewSet ):
    queryset = grid.objects.all()
    #serializer_class = AtlasGridInfoSerializer


# Create your views here.
def view(request):
    #return HttpResponse("처리할 데이터가 없습니다.")
    userlist = account.objects.all()
    context = {'userlist': userlist}
    
    #return render(request, 'view.html', context)
    #return render(request, 'base.html', context)
    if request.method == 'POST':
        
        temp = request.POST.get('monitor_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return render(request, 'atlasgrid/monitor.html', context={'monitor_output': new_hello_world})
    
    else:
        return render(request, 'atlasgrid/monitor.html', context={'text': 'GET METHOD!!!'})