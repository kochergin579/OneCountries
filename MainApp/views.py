from django.shortcuts import render, HttpResponse, redirect
import json
from MainApp.models import Country
from MainApp.models import Language
from django.core.paginator import Paginator




def home(request):
    return render(request, 'index.html')


def countries_list(request):

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

        country = Country.objects.get(id=id)
        languages = country.language.all()

        context = {
            "country": country,
            "languages": languages
        }
        return render(request, "country_page.html", context)


