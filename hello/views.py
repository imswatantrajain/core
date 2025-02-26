from django.shortcuts import render

from django.http import HttpResponse

def hello(request):

    peoples  = [
        {'name' : 'Swatantra', 'age' : '25'},
        {'name' : 'vipul', 'age' : '25'},
        {'name' : 'Somil', 'age' : '25'},
    ]

    # for people in peoples:
    #     print(people)

    vegetables = ['Tomato', 'potato', 'onion']
    return render(request , "index.html" , context = {'peoples' : peoples, 'vegetables' : vegetables, 'page' : 'this is new website page'})

def about(request):
    context = {'page' : 'About'}
    return render(request , "about.html" , context)
def contact(request):
    context = {'page' : 'Contact'}
    return render(request , "contact.html" , context)
def success(request):
    return HttpResponse("<h1>Hey this is a success page.<h1>")
