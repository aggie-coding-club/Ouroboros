from django.conf import settings
from django.db import models

from application.models import DIETARY_RESTRICTIONS

BREAKFAST = "B"
LUNCH = "L"
DINNER = "D"
MIDNIGHT_SNACK = "MS"
MEAL_CHOICES = [
    (BREAKFAST, "Breakfast"),
    (LUNCH, "Lunch"),
    (DINNER, "Dinner"),
    (MIDNIGHT_SNACK, "Midnight Snack"),
]


class Event(models.Model):
    """
    An abstract model (see Django docs: https://docs.djangoproject.com/en/2.2/topics/db/models/#abstract-base-classes)
    for recording activity during the event.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class FoodEvent(Event):
    meal = models.CharField(max_length=14, choices=MEAL_CHOICES)
    restrictions = models.CharField(max_length=14, choices=DIETARY_RESTRICTIONS)


class WorkshopEvent(Event):
    pass
