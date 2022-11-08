from django.db import models
from cloudinary.models import CloudinaryField


class Event(models.Model):
    """
    Main model for meet-up events
    featured in Lingomeets website
    """
    title = models.CharField(
        'Event Title',
        max_length=200,
        unique=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )
    date = models.DateField(
        'Event Date',
        auto_now=False,
        blank=False
    )
    destination = models.CharField(
        'Event Destination',
        max_length=200
    )
    image = CloudinaryField(
        'Event Image',
        default='placeholder'
    )
    description = models.TextField(
        blank=True
    )
    price = models.IntegerField(
        'Event Price',
        default=0
    )
    attendees = models.ManyToManyField(
        User,
        related_name='attendee(s)',
        blank=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_on']
