from django.http import HttpResponse, JsonResponse


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