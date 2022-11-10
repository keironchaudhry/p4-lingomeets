from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
    paginate_by = 3


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
        event = get_object_or_404(queryset, slug=slug)

        review = Review.objects
        reviews = review.filter(is_admin_approved=True)
        reviewed = False
        review_form = ReviewForm()

        return render(
            request,
            'meetup_detail.html',
            {
                'event': event,
                'reviews': reviews,
                'reviewed': reviewed,
                'review_form': review_form
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        POST method for users to post reviews
        """
        queryset = Event.objects
        event = get_object_or_404(queryset, slug=slug)

        review = Review.objects
        reviews = review.filter(is_admin_approved=True)
        reviewed = False
        review_form = ReviewForm()

        if (not reviewed):
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review = review_form.save(commit=False)
                review.event = event
                review.user = request.user
                review.save()
                messages.info(
                    request,
                    'Your review is being approved. Thank you.'
                )
                return HttpResponseRedirect(
                    reverse(
                        'meetup_detail.html',
                        args=[slug])
                )
            else:
                return render(
                    request,
                    'meetup_detail.html',
                    {
                        'event': event,
                        'reviews': reviews,
                        'reviewed': reviewed,
                        'review_form': review_form
                    }
                )
