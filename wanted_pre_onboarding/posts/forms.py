from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_writer",
                    "description", "funding_amount", 
                    "funding_end_date",
                    ]
        
        labels = {
            "product_name": "상품명",
            "product_writer": "작성자",
            "description": "상품설명",
            "funding_amount": "목표금액",
            "funding_end_date": "펀딩 종료일",
        }

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_writer",
                    "description", "funding_end_date",
                    ]