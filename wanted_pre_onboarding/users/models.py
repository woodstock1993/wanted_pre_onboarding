from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]

    name = models.CharField(verbose_name="이름", blank=True, max_length=255)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    # product = models.ManyToManyField(product_model.Product)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})