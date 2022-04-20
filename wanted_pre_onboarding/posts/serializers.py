from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "product_name",
            "product_writer",
            "description",
            "funding_amount",
            "funding_end_date",
        )