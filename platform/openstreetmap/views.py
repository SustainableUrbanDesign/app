from django.conf import settings
from django.http import HttpResponse

def get_osm_data(request):
    html = "<p>Hello</p>"
    return HttpResponse(html)