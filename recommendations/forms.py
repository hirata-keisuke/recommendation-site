from django import forms

from recommendations import models

class BeerStyleForm(forms.ModelForm):
    class Meta:
        model = models.BeerStyle
        fields = ("name", "birth_place", "fermentation", "description")
