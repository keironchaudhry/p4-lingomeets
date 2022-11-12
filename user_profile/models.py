from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Model for database of user profile
    featured on Lingomeets website
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )
    avatar = CloudinaryField(
        'avatar',
        default='placeholder'
    )
    native_language = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    other_language = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    bio = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.user}'

    @property
    def get_avatar(self):
        return self.avatar.url
