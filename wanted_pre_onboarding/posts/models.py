from django.db import models
from wanted_pre_onboarding.users import models as user_model
from django.contrib.auth import get_user_model

User = get_user_model

class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Product(TimeStampedModel):

    product_name = models.CharField(verbose_name='상품명', blank=False, max_length=255)
    product_writer= models.ForeignKey(user_model.User, 
                        null=True, on_delete=models.CASCADE, 
                        )
    description = models.TextField(verbose_name='상품설명', blank=False)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    funding_amount = models.IntegerField(verbose_name='목표금액', blank=True)
    funding_end_date = models.CharField(verbose_name='펀딩 종료일', blank=False, max_length=255)
    users_likes = models.ManyToManyField(user_model.User, related_name='product_user_likes', blank=True)

    def __str__(self):
        return f"{self.product_name}: {self.description}"