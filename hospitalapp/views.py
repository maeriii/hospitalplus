from itertools import count

from django.shortcuts import render,redirect
from hospitalapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def appointment(request):
    if request.method == "POST":
        myAppointment = Appointment2(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']

        )
        myAppointment.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

def contact(request):
    if request.method == "POST":
        contactme = Contactus(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        contactme.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')


def show(request):
    allAppointment2 = Appointment2.objects.all()
    return render(request,'show.html',context={'all': all})
