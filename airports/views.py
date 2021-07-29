from django.shortcuts import render
from .forms import LocationForm
from .models import Airport
from .utils import find_airport


def index(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            airports = Airport.objects.all()
            (found, nearest) = find_airport(airports,
                    form.cleaned_data['latitude'],
                    form.cleaned_data['longitude'])
            if found != None:
                return render(request, 'index.html', {'form': form,
                              'airport': found, 'distance': nearest})
    else:
        form = LocationForm()

    return render(request, 'index.html', {'form': form})

 
