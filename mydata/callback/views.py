from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response
from api import views as api_views

from django.http import HttpResponse
# Create your views here.
def index(request):
    return api_views.small_data_callback_handler(request)
