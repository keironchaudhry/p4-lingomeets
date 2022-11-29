from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from review.models import Review
from review.forms import ReviewForm
from .models import Event


class PastMeetups(generic.ListView):
    """
    View for past meetups in website
    """
    model = Event
    queryset = Event.objects.order_by('-created_on')
    template_name = 'past_meetups.html'
    paginate_by = 4


class MeetupView(View):
    """
    View for rendering meet up
    event detail page in website
    """
    def get(self, request, slug, *args, **kwargs):
        """
        GET method to get meetup post and reviews
        """
        queryset = Event.objects
        event = get_object_or_404(
            queryset,
            slug=slug
        )

        reviews = event.reviews.filter(
            is_admin_approved=True
        )
        reviewed = False

        attending = False
        if event.attendees.filter(
            id=request.user.id
        ).exists():
            attending = True

        review_form = ReviewForm()

        return render(
            request,
            'meetup_detail.html',
            {
                'event': event,
                'reviews': reviews,
                'reviewed': reviewed,
                'attending': attending,
                'review_form': review_form
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        POST method for users to post reviews
        """
        queryset = Event.objects
        event = get_object_or_404(
            queryset,
            slug=slug
        )

        reviews = event.reviews.filter(
            is_admin_approved=True
        )
        reviewed = False

        attending = False
        if event.attendees.filter(
            id=request.user.id
        ).exists():
            attending = True

        review_form = ReviewForm(
            data=request.POST
        )

        if (not reviewed):
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review = review_form.save(
                    commit=False
                )
                review.event = event
                review.user = request.user
                review.save()
                messages.info(
                    request,
                    'Your review is being approved. Thank you.'
                )
                return HttpResponseRedirect(
                    reverse(
                        'meetup_detail',
                        args=[slug]
                    )
                )
            else:
                return render(
                    request,
                    'meetup_detail.html',
                    {
                        'event': event,
                        'reviews': reviews,
                        'reviewed': reviewed,
                        'attending': attending,
                        'review_form': review_form
                    }
                )


class AttendeeRegistration(View):
    """
    View for rendering attendee
    registration using a toggle button
    """
    def get(self, request, *args, **kwargs):
        """
        GET method for registered attendees
        """
        event = Event.objects.order_by('-date').filter(
            attendees=request.user
        )

        return render(
            request,
            'meetup_detail.html',
            {
                'event': event,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        POST method for registering attendees
        """
        queryset = Event.objects
        event = get_object_or_404(
            queryset,
            slug=slug
        )

        if event.attendees.filter(
            id=request.user.id
        ).exists():
            event.attendees.remove(
                request.user
            )
        else:
            event.attendees.add(
                request.user
            )

        return HttpResponseRedirect(
            reverse(
                'meetup_detail',
                args=[slug]
                )
            )
