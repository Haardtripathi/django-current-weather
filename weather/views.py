from django.shortcuts import render,redirect
import json
import urllib.request
from datetime import datetime 
# Create your views here.

def index(request):
    if(request.method=="POST"):
        city=request.POST['city']

        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=58c76fd0cfcb08c51c095737700b67e6&units=metric').read()

        json_data=json.loads(res)
        print(json_data)
        data={
            "temp":str(json_data['main']['temp']),
            "wind":str(json_data['wind']['speed']),
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "min":str(json_data['main']['temp_min']),
            "max":str(json_data['main']['temp_max']),

            "cloud":str(json_data['clouds']['all'])+"%"
        }

        
        return render(request,'index.html',{'data':data,'city':city})
    else:
        return render(request,'index.html')