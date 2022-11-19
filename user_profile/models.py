from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import date
from lingomeets.validators import validate_textfields


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
        blank=True,
        validators=[validate_textfields]
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - (
                (
                    today.month, today.day
                ) < (
                    self.birthday.month, self.birthday.day
                    )
            )
            return age
        else:
            return ''

    @property
    def get_avatar(self):
        return self.avatar.url
