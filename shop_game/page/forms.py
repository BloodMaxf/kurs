from .models import Product
from django.forms import ModelForm

class Purchased(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'