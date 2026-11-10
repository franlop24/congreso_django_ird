from django.shortcuts import render

from .models import Workshop

# Create your views here.
def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        "workshops": workshops
    }
    return render(request, 'workshop/list.html', context)