from django import forms
from django.core import validators
from index import models


class MusicianForm(forms.ModelForm):
    
    class Meta:
        model = models.Musician
        fields = "__all__"


# class user_form(forms.Form):
    
#     user_name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
#     user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type':'date'}))
#     user_email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder':'Enter your email', 'style':'width:300px'}))
#     user_password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    
#     def clean(self):
#         all_clean_data = super().clean()
#         password = all_clean_data['user_password']
#         confirm = all_clean_data['confirm_password']
        
#         if password != confirm:
#             raise forms.ValidationError("Password Fields Not Matched")
        
    
