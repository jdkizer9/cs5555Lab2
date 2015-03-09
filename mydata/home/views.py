from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response
from django.http import HttpResponseRedirect


from django.http import HttpResponse
from controllers.my_data_network_controller import DPUNetworkController, GithubNetworkController


clientName = ""
githubClientName = ""

def RegisterPrimaryClient():
    print "RegisterPrimaryClient"
    if(not DPUNetworkController.CheckForClient(clientName)):
        client = DPUNetworkController(clientName, '5555-2015-????', '?????')
        DPUNetworkController.RegisterClient(clientName, client)

    if(not GithubNetworkController.CheckForClient(githubClientName)):
        githubClient = GithubNetworkController(githubClientName, '80f75c86d218df2dd193', '0f033172a95f612dbcf88f9ae3c711127e926776')
        GithubNetworkController.RegisterClient(githubClientName, githubClient)

# Create your views here.
def index(request):
    #check for authenticated user
    #Assume primary client exists
    dpu_client = DPUNetworkController.GetClient(clientName)
    if(not dpu_client.is_client_authenticated()):
        if(clientName ==""):
            print '@@@@@@@@@@@@'
            t = loader.get_template("home/Login.html")
            html = t.render(Context({}))
            return HttpResponse(html)
        print 'Client is NOT authenticated'
        url = dpu_client.get_authorize_url()
        return HttpResponseRedirect(url)

    print 'Client is authenticated'
    t = loader.get_template("home/index.html")
    html = t.render(Context({}))
    return HttpResponse(html)


def index(request):
    #check for authenticated user
    #Assume primary client exists
    dpu_client = DPUNetworkController.GetClient(clientName)
    if(not dpu_client.is_client_authenticated()):
        if(clientName ==""):
            print '@@@@@@@@@@@@'
            t = loader.get_template("home/Login.html")
            html = t.render(Context({}))
            return HttpResponse(html)
        print 'Client is NOT authenticated'
        url = dpu_client.get_authorize_url()
        return HttpResponseRedirect(url)

    print 'Client is authenticated'
    t = loader.get_template("home/index.html")
    html = t.render(Context({}))
    return HttpResponse(html)

RegisterPrimaryClient()
