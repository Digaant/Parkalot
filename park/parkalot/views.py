from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from django.template import loader,RequestContext
import pyqrcode
# Create your views here.
def index(request):
    k=user.objects.order_by('-star_time')[:5]
    template = loader.get_template('parkalot/index.html')
    context={
        'k':k,
             }
    return HttpResponse(template.render(context,request))
def detail(request,k):
    carn=user.objects.get(carnum=k)
    return render(request,'parkalot/details.html',{'carn': carn,})
def qr(request):
    last = user.objects.order_by('-star_time')[:5]
    for i in last:
        break
    ustr="http://10.5.62.44:8080/parkalot/"+i.carnum
    qr = pyqrcode.create(ustr)
    return render(request,'parkalot/qrgenerator.html',{'ustr':ustr})
