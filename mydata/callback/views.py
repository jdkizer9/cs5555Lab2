from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response
from api import views as api_views
from django.http import HttpResponseRedirect
from controllers.my_data_network_controller import DPUNetworkController

from django.http import HttpResponse
# Create your views here.

clientName = 'james'

def index(request):
    print "in callback hander"
    code = request.GET['code']
    dpu_client = DPUNetworkController.GetClient(clientName)
    dpu_client.configure_access_token(code)
    return HttpResponseRedirect('/home/')

    # return api_views.small_data_callback_handler(request)
