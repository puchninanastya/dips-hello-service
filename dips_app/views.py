# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	 return render(request, 'dips_app/index.html', {})

def hello(request):
	if 'name' in request.GET and request.GET['name']:
		name = request.GET['name']
		return HttpResponse("<h1>Hello, " + name + "!</h1>")
	else:
		return HttpResponse("<h1>Hi!</h1>")