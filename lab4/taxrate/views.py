from django.shortcuts import render

tax_rate = ["15%"]

def index(request ):
    return render(request , "taxrate/index.html", {
        "tax_rate": tax_rate
    })
