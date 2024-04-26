from django import forms
from .models import hoteldetails, staffmanagement


class hoteldetailsform(forms.ModelForm):
    class Meta:
        model = hoteldetails
        fields = '__all__'


class hotelstaffmanagement(forms.ModelForm):
    class Meta:
        model = staffmanagement
        fields = '__all__'