from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import datetime


def main(request):
    return HttpResponse("<h3> <center>welcome to my project </center> </h3> ")


def api_movie(request, item: str) -> str:
    api = {
        "name": "Pulp fiction",
        "year": 1992,
        "director": "quetin tarantino",
        "active": True
    }
    try: 

        if api[item]:
            message = api[item]
    except KeyError:
            message = "Error 404"
        
    return HttpResponse(message)


def index(request):
     frameworks = ["Laravel", ".Net", "Django", "Express", "ASP.NET" ]
     context = {"date": datetime.datetime.now(), "frameworks": frameworks}
     return render(request, "index.html", context=context)


def father(request):
    return render(request, "father.html")


def carlos(request):
     return render(request, "carlos.html")