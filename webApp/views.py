from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import SaleProduct
import datetime


# Create your views here.
def main_page(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["list"] = SaleProduct.objects.all()

    return render(request, "main_page.html", context)
