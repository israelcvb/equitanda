from django.shortcuts import HttpResponse


def catalog(request):
    site_name = "Moderne Musician"
    response_html = f"<html><body>Welcome to {site_name}.</body></html>"
    return HttpResponse(response_html)
