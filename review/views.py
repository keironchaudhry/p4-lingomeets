from django.http import HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, reverse, get_object_or_404
from event.models import Event
from .models import Review


class EditReview(generic.UpdateView):
    """
    View for editing a review and
    returning to meetup detail page
    """
    model = Review
    fields = ['content', 'rating']
    template_name = 'edit_review.html'

    def get_success_url(self) -> str:

        slug = self.object.event.slug
        return reverse('meetup_detail', args=[slug])


class DeleteReview(View):
    """
    View for deleting a user-made review
    and returning to meetup detail page
    """
    def post(self, request, slug, *args, **kwargs):
        event = get_object_or_404(Event, slug=slug)
        review = Review.objects.filter(user=request.user)
        review.delete()

        return HttpResponseRedirect(reverse('meetup_detail', args=[slug]))
