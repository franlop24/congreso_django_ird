from django.shortcuts import render, get_object_or_404

from .models import Workshop

# Create your views here.
def workshop_list(request):
    workshops = Workshop.objects.all()
    context = {
        "workshops": workshops
    }
    return render(request, 'workshop/list.html', context)

def workshop_details(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    context = {
        "workshop": workshop
    }
    return render(request, "workshop/details.html", context)