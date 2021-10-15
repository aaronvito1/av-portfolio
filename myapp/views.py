import requests
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import models
from .models import Post

# Create your views here.
def index(request):
	print('home page being visited')
	context = {
	}
	return render(request, "index.html", context)

def about(request):
	print('about page being visited')
	context={

	}
	return render(request, "about.html", context)

def portfolio(request):
	print('portfolio page being visited')
	context={

	}
	return render(request, "portfolio.html", context)

def contact(request):
	print('contact page being visited')
	context={

	}
	return render(request, "contact.html", context)

