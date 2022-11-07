from django.shortcuts import render
from django.views import generic

# Create your views here.


class PastMeetups(generic.TemplateView):
    """
    View for past meetups in website
    """
    template_name = 'past_meetups.html'
