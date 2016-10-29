from django import forms
from django.forms import ModelForm
from .models import NewClinic


class NewClinicForm(forms.Form):
    clinic_name = forms.CharField(label='Clinic Name', max_length=50)
    excel_file = forms.FileField(label= 'Reference File (.xlsx ONLY)')
    zip_file = forms.FileField(label= '.edf Files (.zip ONLY)')


    #widget=forms.TextInput(),

# class NewClinicForm(ModelForm):
#     class Meta:
#         model = NewClinic
#         fields = '__all__'