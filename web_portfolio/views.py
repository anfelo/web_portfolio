from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

from . import forms


def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def contact(request):
	form = forms.ContactForm()	
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():	
			send_mail(
				'Message from {}'.format(form.cleaned_data['name']),
				form.cleaned_data['message'],
				'{name} <{email}>'.format(**form.cleaned_data),
				['af.osorio1341@gmail.com']				
			)
			messages.add_message(request, messages.SUCCESS,
									'Thanks for your message!')
			return HttpResponseRedirect(reverse('contact'))
	return render(request, 'contact.html', {'form': form})


def work(request):
	return render(request, 'work.html')
