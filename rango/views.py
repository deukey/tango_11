from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Hyperdog."}
    return render(request, 'rango/about.html', context=context_dict)
