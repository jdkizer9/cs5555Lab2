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


@api_view(['GET', 'POST'])         ### replaces JSONResponse(Htttpresponse)
def smal_data_authentication(request):
    print("user_daily_mobility_segments")
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # return HttpResponse(json.dumps(response_data), content_type="application/json")


    omh = OAuth2Service(
        name=omhName,
        client_id=client_id,
        client_secret=client_secret,
        access_token_url='https://ohmage-omh.smalldata.io/dsu/oauth/token',
        authorize_url='https://ohmage-omh.smalldata.io/dsu/oauth/authorize',
        base_url='https://ohmage-omh.smalldata.io/dsu/'
        )

    params = {'redirect_uri': "http://127.0.0.1:8000/callback",'response_type': 'code' }

    url = omh.get_authorize_url(**params)
    return HttpResponseRedirect(url)


@api_view(['GET', 'POST'])         ### replaces JSONResponse(Htttpresponse)
def user_daily_mobility_segments(request):
    print("user_daily_mobility_segments")
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    # return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps(response_data), content_type="application/json")
