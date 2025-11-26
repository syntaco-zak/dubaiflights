from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Choice


def index(request):
    flights = Flight.objects.order_by('-created_at')[:5]
    return render(request, 'flights/index.html', {"flights": flights})



def detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, 'flights/detail.html', {"flight": flight})



def vote(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    try:
        
        selected_choice = flight.choice_set.get(id=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, "flights/detail.html", {
            "flight": flight,
            "error_message": "Please choose an option before voting."
        })

    
    selected_choice.votes += 1
    selected_choice.save()

    
    return HttpResponseRedirect(reverse("flights:results", args=(flight.id,)))



def results(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    return render(request, "flights/results.html", {"flight": flight})
