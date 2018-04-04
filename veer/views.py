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
