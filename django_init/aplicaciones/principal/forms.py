from django import forms
from .models import Productos
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'