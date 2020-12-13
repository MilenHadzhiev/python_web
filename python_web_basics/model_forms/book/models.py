from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.PositiveIntegerField(
        default=0,
        validators=(
            MinValueValidator(
                1,
                message='Your book must have at least one page.'
            ),
        )
    )
    description = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=20)
