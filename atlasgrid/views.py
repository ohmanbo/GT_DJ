from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import account, grid, HelloWorld
from rest_framework import viewsets
from django.urls import reverse

import logging

logger = logging.getLogger(__name__)


class AtlasGridInfo( viewsets.ModelViewSet ):
    queryset = grid.objects.all()
    #serializer_class = AtlasGridInfoSerializer


# Create your views here.
def view(request):
    userlist = account.objects.all()
    context = {'userlist': userlist}
    
    if request.method == 'POST':
        
        monitor_input_text = request.POST.get('monitor_input')
        if monitor_input_text:
            new_hello_world = HelloWorld()
            new_hello_world.text = monitor_input_text
            new_hello_world.save()     
            logger.debug("save 완료")     
                
        
        return HttpResponseRedirect(reverse('monitor'))
    
    else:
        logger.debug("비 POST 요청 완료 aka 페이지 재 로드")
        hello_world_list = HelloWorld.objects.all()
        hello_world_list_reversed = hello_world_list[::-1]
        return render(request, 'atlasgrid/monitor.html', context={'monitor_output': hello_world_list_reversed})