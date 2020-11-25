
from django.shortcuts import render
import requests
from rest_framework import viewsets
import datetime
from django.http import HttpResponse
from .serializers import MemberSerializer
from .models import Member
def home(request):

  
    response = requests.get('http://dummy.restapiexample.com/api/v1/employees')
          
    
    return HttpResponse(response.json().get('data'))
   
    '''print(geodata)
    context={'id': geodata['id'],
        'employee_name': geodata['employee_name'],
        'employee_age': geodata['employee_age'],
        'employee_salary': geodata['employee_salary'],
        

    }'''
   


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer



