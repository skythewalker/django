from django import forms
from .models import MiniAppCategory


class MiniAppCategoryForm(forms.Form):
    app_varieties = forms.ModelChoiceField(queryset= MiniAppCategory.objects.all(), label="Select provider types")