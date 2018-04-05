# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# Return to index.html on loading home page
def index(request):
    context = {"navbar": "profile"}
    return render(request, "application/index.html", context)


def education(request):
	context = {"navbar": "education"}
	return render(request, "application/education.html", context)


def experience(request):
	context = {"navbar": "experience"}
	return render(request, "application/experience.html", context)


def skills(request):
	context = {"navbar": "skills"}
	return render(request, "application/wip.html", context)


def certifications(request):
	context = {"navbar": "certifications"}
	return render(request, "application/certifications.html", context)


def publications(request):
	context = {"navbar": "publications"}
	return render(request, "application/publications.html", context)


def contact(request):
	context = {"navbar": "contact"}
	return render(request, "application/wip.html", context)
