from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response
from django.http import HttpResponseRedirect


from django.http import HttpResponse
from controllers.my_data_network_controller import DPUNetworkController

clientName = 'james'

def RegisterPrimaryClient():
    print "RegisterPrimaryClient"
    if(not DPUNetworkController.CheckForClient(clientName)):
        client = DPUNetworkController(clientName, '5555-2015-james', 'QNQADNryoP')
        DPUNetworkController.RegisterClient(clientName, client)

# Create your views here.
def index(request):


    #check for authenticated user
    #Assume primary client exists
    dpu_client = DPUNetworkController.GetClient(clientName)
    if(not dpu_client.is_client_authenticated()):
        print 'Client is NOT authenticated'
        url = dpu_client.get_authorize_url()
        return HttpResponseRedirect(url)

    print 'Client is authenticated'
    t = loader.get_template("home/index.html")
    # return HttpResponse(template.render(c))
    html = t.render(Context({}))
    return HttpResponse(html)

RegisterPrimaryClient()