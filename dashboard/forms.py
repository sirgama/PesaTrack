from django import forms
from .models import Expenses, Categories

class NewExpenditureForm(forms.ModelForm):
    description =forms.CharField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Description of what youve spent on'}), required=True)
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'Input', 'placeholder': 'Cost'}), required=True)
    
    class Meta:
        model = Expenses
        fields = ['category', 'description', 'amount']