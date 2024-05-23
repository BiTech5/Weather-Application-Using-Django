from django.shortcuts import render
# Create your views here.
from . import weather_fetch
def index(request):
    city=''
    if request.method=='POST':
        API_KEY='Enter Your API KEY'
        city=request.POST.get("city",'default')
        # city=request.POST['city']
        city=str(city)
        if city=='':
            wea_info='empty'
        else:
            wea_info=weather_fetch.weather(city,API_KEY)
        print(wea_info)
        city=(city).capitalize()
        print(city)
        # print(wea_info['city'])
    else:
        wea_info={}
    return render(request,'index.html',{'wea_info':wea_info,
                                        'city':city,})     
    # return render(request,'index.html')


    