from django import forms
from django.forms import ModelForm
from .models import *

## FORMS HAVE NOT BEEN IMPLEMENTED TO TEMPLATES FOR THE MIDTERM AS ONLY REST END POINTS SPECIFIED

class AirlineForm(ModelForm):
    class Meta:
        model = Airlines
        fields = ['name', 'alias', 'iata', 'icao', 'callsign', 'active', 'country']

        def clean(self):
            cleaned_data = super(AirlineForm, self).clean()
            active = cleaned_data.get("active")

            if not active == "Y" and not active == "N":
                raise forms.ValidationError("Active must be 'Y' or 'N'")
            
            return(cleaned_data)