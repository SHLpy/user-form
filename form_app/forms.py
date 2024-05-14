from django import forms
from form_app.models import UserDetails

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'email', 'age']
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise forms.ValidationError("Name must be at least 5 characters long.")
        return name
    
    def clean_email(self):
        email =self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Please use an email address from gmail.com domain.")
        return email