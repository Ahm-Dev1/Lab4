from django.shortcuts import render

def index(request , num):
    return render(request, 'anyNumber/index.html',{
        'num': num + (num*0.15)
    })
