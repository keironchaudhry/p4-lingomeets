from django.db import models
from django.contrib.auth.models import User
from event.models import Event


class Review(models.Model):
    """
    Review database model for reviews
    made by users in Lingomeets website
    """
    SCORE = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_reviews'
    )
    content = models.TextField(
        blank=True
    )
    rating = models.IntegerField(
        choices=SCORE,
        default=3
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )
    is_admin_approved = models.BooleanField(
        default=False
    )
