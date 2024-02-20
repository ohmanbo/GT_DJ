from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import account, grid, HelloWorld
from rest_framework import viewsets
from django.http import JsonResponse
from django.core import serializers
import json

import logging

logger = logging.getLogger(__name__)


class AtlasGridInfo( viewsets.ModelViewSet ):
    queryset = grid.objects.all()
    #serializer_class = AtlasGridInfoSerializer


# Create your views here.
def view(request):
    userlist = account.objects.all()
    context = {'userlist': userlist}

    content_type = request.META.get('CONTENT_TYPE') # CONTENT_TYPE 대문자로 써야함.
    #print(f"HTTP request method: {request.method} content-type: {content_type}")

    if request.method == 'POST':
        
        monitor_input_text = request.POST.get('monitor_input')
        if monitor_input_text:
            new_hello_world = HelloWorld(text=monitor_input_text)
            new_hello_world.save()     
            #print(f"save 완료 내용 {monitor_input_text}")     
                
        # 최신 10개의 HelloWorld 객체 가져오기
        hello_world_list = HelloWorld.objects.all().order_by('-id')[:30]
        # QuerySet을 JSON으로 직렬화
        data = serializers.serialize('json', hello_world_list)
        
        return JsonResponse({'success': True, 'data': data})
    elif request.method == 'GET':
        
        requested_data = request.GET.get('what', default='def')
        
        if( requested_data == 'gridinfo'):
            print("GET.gridinfo 호출")
            
            # 여기에서 griddata.json 파일을 읽습니다.
            try:
                with open('griddata.json', 'r') as file:
                    grid_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"파일을 읽는 중 오류 발생: {e}")
                grid_data = []  # 오류 발생 시 빈 리스트 또는 기본값 할당
            
            #hello_world_list = HelloWorld.objects.all().order_by('-id')[:30]
        
            context = {
                #'monitor_output': hello_world_list,
                'grid_data': grid_data,
            }
            return JsonResponse({'success': True, 'data': context})
        else:
            print("GET.def 호출")
            hello_world_list = HelloWorld.objects.all().order_by('-id')[:30]
        
            context = {
                'monitor_output': hello_world_list
            }
            return render(request, 'atlasgrid/monitor.html', context)
        
    else:
        print("request.method 가 명시되지 않음. GET.def 호출")
        hello_world_list = HelloWorld.objects.all().order_by('-id')[:30]
        
        context = {
            'monitor_output': hello_world_list
        }
        
        return render(request, 'atlasgrid/monitor.html', context)