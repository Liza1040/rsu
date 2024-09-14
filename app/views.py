from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def index_page(request: WSGIRequest):
    context = {"time": datetime.now()}
    return render(request, "index.html", context)
