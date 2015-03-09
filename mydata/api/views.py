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
import matplotlib.pyplot as plt
#from rauth import OAuth2Service


clientName = 'james'

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

@api_view(['GET'])
def user_pam_figure(request):
    print "user_pam_data"
    if(DPUNetworkController.GetClient(clientName)):
        dpu_client = DPUNetworkController.GetClient(clientName)
        print dpu_client.access_token
        response = dpu_client.getPAMData()
        pam_json = response.json()

        #generate data from JSON
        valence_list = []
        arousal_list = []
        for entry in pam_json:
            body = entry['body']
            valence_list.append(body['affect_valence'])
            arousal_list.append(body['affect_arousal'])

        if(len(valence_list) > 0):
            average_valence = reduce( lambda a, x: a+x, valence_list) / float(len(valence_list))
            average_arousal = reduce( lambda a, x: a+x, arousal_list) / float(len(arousal_list))
            plt.scatter(valence_list, arousal_list, s=100, c='b', alpha=0.5)
        else:
            average_valence = 0.0
            average_arousal = 0.0

        # plot data
        plt.scatter([average_valence], [average_arousal], s=100, c='r', alpha=0.5)


        # draw vertical line from (70,100) to (70, 250)
        plt.plot([2.5, 2.5], [0, 5], 'k-')

        # draw diagonal line from (70, 90) to (90, 200)
        plt.plot([0, 5], [2.5, 2.5], 'k-')
        plt.figure(num=1, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')

        ax = plt.axes()
        ax.set_xlim(left=0, right=5)
        ax.set_ylim(bottom=0, top=5)

        plt.xlabel('Valence')
        plt.ylabel('Arousal')

        #return plot
        response = HttpResponse(content_type="image/png")
        plt.savefig(response, format="png")
        plt.close()
        return response
    # # return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponseBadRequest
