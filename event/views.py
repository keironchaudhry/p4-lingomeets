from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.


class PastMeetups(generic.ListView):
    """
    View for past meetups in website
    """
    model = Event
    queryset = Event.objects.order_by('-created_on')
    template_name = 'past_meetups.html'
    paginate_by = 3
