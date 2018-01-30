from django import forms
from django.core import validators


def must_be_empty(value):
	if value:
		raise forms.ValidationError('is not empty')


class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control',
														'required': True}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control', 
															'required': True}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 
															'required': True}))
	honeypot =	forms.CharField(required=False, 
								widget=forms.HiddenInput, 
								label="Leave empty",
								validators=[must_be_empty])
