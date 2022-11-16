from django.shortcuts import render
from django.views import generic
from event.models import Event


class HomeView(generic.ListView):
    """
    View for the landing page template of website
    """
    model = Event
    queryset = Event.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 1
