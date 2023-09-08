from django.shortcuts import render, HttpResponse, redirect
import json
from MainApp.models import Country
from MainApp.models import Language

from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, 'index.html')


def countries_list(request):
    #
    country = Country.objects.all()


    context = {
            "country": country

    }
    return render(request, "countries_list.html", context)


def languages_list(request):
    language = Language.objects.all()
    # with open('countries.json') as f:
    #
    #     country = json.load(f)
        # for languages in country:
        #     for language in languages.languages:
    context = {
            "language": language
        }
    return render(request, "languages_list.html", context)

def country_page(request, id):
     # try:
    country = Country.objects.get(id=id)
        # language = Country.Language.all()
     # except ObjectDoesNotExist:
     #    return HttpResponseNotFound(f"Товар с id {id} не найден")
    context = {
        "country": country
            # "language": language
    }
    return render(request, "country_page.html", context)
