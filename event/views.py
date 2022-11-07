from django.shortcuts import render
from django.views import generic

# Create your views here.


class PastEvents(generic.TemplateView):
    """
    View for the landing page template of website
    """
    template_name = 'past_events.html'
