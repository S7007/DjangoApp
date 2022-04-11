from django.shortcuts import render
from django.contrib import messages

from Goodway.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "Nature is Everything"
    }
    #messages.success(request, "Hello How R U")
    return render(request,'index.html', context)
    
    #return HttpResponse("THIS IS MY HOMEPAGE")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("THIS IS MY AboutPAGE")


def services(request):
    return render(request,'services.html')
    #return HttpResponse("THIS IS MY ServicePAGE")

def cobing(request):
    return render(request,'cobing.html')

def shopping(request):
    return render(request,'shopping.html')

def novel(request):
    return render(request,'novel.html')

def videoc(request):
    return render(request,'videoc.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your Form Is Submitted.')

        
    return render(request,'contact.html')
    #return HttpResponse("THIS IS MY ContactPAGE")
