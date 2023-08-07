from django.shortcuts import render, HttpResponse
import json


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    with open('countries.json') as f:
        country = json.load(f)

        context = {
            "country": country

        }
    return render(request, "countries_list.html", context)


def languages_list(request):
    with open('countries.json') as f:
        country = json.load(f)

        context = {
            "country": country
        }
    return render(request, "languages_list.html", context)
