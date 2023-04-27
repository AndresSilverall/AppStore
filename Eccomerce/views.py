from django.http import HttpResponse


def main(request):
    return HttpResponse("<h3> <center>welcome to my project </center> </h3> ")