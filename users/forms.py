from django import forms
from django.contrib.auth.models import User
from . models import Profile

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    names = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
   

    class Meta:
        model = Profile
        fields=['image', 'names', 'bio']