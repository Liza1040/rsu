from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def index_page(request: WSGIRequest):
    context = {
        'data':[
            {
            'name': "Доски",
            'description': "Супер крутые прочные доски"
            },
            {
                'name': "Доски",
                'description': "Супер крутые прочные доски"
            },
            {
                'name': "Доски",
                'description': "Супер крутые прочные доски"
            },
            {
                'name': "Доски",
                'description': "Супер крутые прочные доски"
            },
            {
                'name': "Доски",
                'description': "Супер крутые прочные доски"
            },
            {
                'name': "Доски",
                'description': "Супер крутые прочные доски"
            },
        ],
    }
    return render(request, "main_page.html", context)

