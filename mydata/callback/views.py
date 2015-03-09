from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response
from api import views as api_views
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from controllers.my_data_network_controller import DPUNetworkController

from django.http import HttpResponse
# Create your views here.

clientName = 'zaf'

def index(request):
    #print "in callback hander"
    code = request.GET['code']
    dpu_client = DPUNetworkController.GetClient(clientName)
    dpu_client.configure_access_token(code)
    return HttpResponseRedirect('/home/')

    # return api_views.small_data_callback_handler(request)

@api_view(['GET'])
def github_callback(request):
	return HttpResponse("Github callback!!")
    # code = request.GET['code']
    # dpu_client = DPUNetworkController.GetClient(clientName)
    # dpu_client.configure_access_token(code)
    # return HttpResponseRedirect('/home/')
