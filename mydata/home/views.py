from django.shortcuts import render
from django.template import Context, loader
from django.shortcuts import redirect ,render_to_response


from django.http import HttpResponse
# Create your views here.
def index(request):

    t = loader.get_template("home/index.html")
    # return HttpResponse(template.render(c))
    html = t.render(Context({}))
    return HttpResponse(html)
