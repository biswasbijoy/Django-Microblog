from django.db import models
from dbpost.models.core_models import BaseStampStampModel


class PostCategory(BaseStampStampModel):
    CATEGORY_OPTION_CHOICES = (
        ('Cat_one', 'Category one',),
        ('Cat_two', 'Category two',),
        ('Cat_three', 'Category three',),
    )

    category = models.CharField(max_length=50, choices=CATEGORY_OPTION_CHOICES, default='Cat_one')
    value = models.PositiveIntegerField(default=0)
