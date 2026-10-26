from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    users = User.objects.all()
    context = { "users": users }
    return render(request, 'home/about.html', context)

def contact(request):
    utt = {
        "name": "Universidad Tecnológica de Tlaxcala",
        "short_name": "UTT",
        "phone": "2474725300",
        "url": 'https://uttlaxcala.edu.mx'
    }
    context = { "utt": utt }
    return render(request, 'home/contact.html', context)

