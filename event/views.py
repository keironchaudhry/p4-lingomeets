from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class MeetupView(View):
    """
    View for rendering meet up 
    event detail page in website
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects
        event = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'meetup_detail.html',
            {
                'event': event,
            }
        )
