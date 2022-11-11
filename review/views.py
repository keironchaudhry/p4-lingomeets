from django.views import generic
from django.shortcuts import render, reverse
from .models import Review


class EditReview(generic.UpdateView):
    """
    View for editing a review and
    returning to meetup detail template
    """
    model = Review
    fields = ['content', 'rating']
    template_name = 'edit_review.html'

    def get_success_url(self) -> str:

        slug = self.object.event.slug
        return reverse('meetup_detail', args=[slug])
