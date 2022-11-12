from django.shortcuts import render

from stocks import models

# Create your views here.
def home(request):
    stocks = models.Stock.objects.all()
    context = {
        'stocks': stocks
    }
    return render(request, 'stocks/home.html', context)
