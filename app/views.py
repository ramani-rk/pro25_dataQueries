from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

def create_school(request):
    if request.method=='POST':
        School_name=request.POST['sn']
        School_location=request.POST['sl']
        school_principal=request.POST['sp']

        SO=School.objects.get_or_create(School_name=School_name,School_location=School_location,school_principal=school_principal)[0]
        SO.save()
        
        TO=School.objects.all()
        d={'create':TO}
        return render(request,'school_datas.html',d)

    return render(request,'create_school.html')

