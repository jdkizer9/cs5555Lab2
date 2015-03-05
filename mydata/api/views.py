import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse ,HttpResponseRedirect
from django.template import RequestContext, loader , Context
from django.shortcuts import redirect ,render_to_response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from controllers.my_data_network_controller import DPUNetworkController
#from rauth import OAuth2Service


clientName = 'zaf'

@api_view(['GET'])         ### replaces JSONResponse(Htttpresponse)
def user_daily_mobility_segments(request):
    print "user_daily_mobility_segments"
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getMobilityDailySegmentsData()
        # return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(response, content_type="application/json")
    else:
        return HttpResponseBadRequest

@api_view(['GET'])         ### replaces JSONResponse(Htttpresponse)
def user_daily_mobility_summary(request):
    print "user_daily_mobility_summary"
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getMobilityDailySummaryData()
        return HttpResponse(response, content_type="application/json")
    else:
        return HttpResponseBadRequest

@api_view(['GET'])
def user_pam_data(request):
    print "user_pam_data"
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getPAMData()
        return HttpResponse(response, content_type="application/json")
    # # return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponseBadRequest
