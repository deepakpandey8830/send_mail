# forms.py
from django import forms

class ContactForm(forms.Form):
    how_did_you_find_us = forms.ChoiceField(
        choices=[
            ('Advertisement', 'Advertisement'),
            ('One', 'One'),
            ('Two', 'Two'),
            ('Three', 'Three'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg: Thomas Adison'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@snuff.com'})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'})
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your subject'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your message', 'rows': 6})
    )
    agree_to_terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )