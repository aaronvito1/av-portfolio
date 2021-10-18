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
	# content_html = open("apps/core/templates/portfolio.html").read()
	print('Portfolio page being visited')
	response = requests.get('https://api.github.com/users/aaronvito1/repos')
	repos = response.json()
	context = {
		'github_repos': repos, 
	}
	return render(request, "portfolio.html", context)


def extra(request):
	# content_html = open("apps/core/templates/extra.html").read()
	print('Extra page being visited')
	context = {
		# "content": content_html, 
	}
	return render(request, "extra.html", context)
	
def contact(request):
	print('contact page being visited')
	context={

	}
	return render(request, "contact.html", context)

