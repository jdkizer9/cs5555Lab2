import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import RequestContext, loader , Context
from django.shortcuts import redirect ,render_to_response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rauth import OAuth2Service
from my_data_network_controller import DPUNetworkController

clientName = 'james'

def RegisterPrimaryClient():
    if(not DPUNetworkController.CheckForClient(clientName)):
        client = DPUNetworkController(clientName, '5555-2015-*****', '*********')
        DPUNetworkController.RegisterClient(clientName, client)

@api_view(['GET', 'POST'])         ### replaces JSONResponse(Htttpresponse)
def smal_data_authentication(request):
    print("user_daily_mobility_segments")

    dpu_client = DPUNetworkController.GetClient(clientName)
    url = dpu_client.get_authorize_url()

    return HttpResponseRedirect(url)

@api_view(['GET', 'POST'])
def small_data_callback_handler(request):
    code = request.GET['code']
    dpu_client = DPUNetworkController.GetClient(clientName)

    dpu_client.configure_access_token(code)

    return HttpResponseRedirect('/api/user_pam_data/')


@api_view(['GET'])         ### replaces JSONResponse(Htttpresponse)
def user_daily_mobility_segments(request):
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getMobilityDailySegmentsData()
        return HttpResponse(response.json(), content_type="application/json")
    else:
        return HttpResponseBadRequest

@api_view(['GET'])         ### replaces JSONResponse(Htttpresponse)
def user_daily_mobility_summary(request):
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getMobilityDailySummaryData()
        return HttpResponse(response.json(), content_type="application/json")
    else:
        return HttpResponseBadRequest

@api_view(['GET'])
def user_pam_data(request):
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getPAMData()
        return HttpResponse(response.json(), content_type="application/json")
    else:
        return HttpResponseBadRequest

RegisterPrimaryClient()
