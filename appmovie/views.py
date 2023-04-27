from django.shortcuts import render
from .forms import ApiForm

# Create your views here.
def api_movie(request):
    form = ApiForm()
    context = {"form": form}
    return render(request, "form.html", context=context )
