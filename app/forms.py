__author__ = 'diego'

from django import forms


# Form to validate percentage
class PercentageForm(forms.Form):
    percentage = forms.IntegerField(label='Procentaje', min_value=1, max_value=99)
