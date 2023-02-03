from .forms import *
from django.shortcuts import render
# Create your views here.
def home(request):
    search_reference = SearchReferenceForm(request.GET)
    queries = None
    if search_reference.is_valid():
        queries = Query.objects.filter(slug = search_reference)
    return render(request,"services/home.html",{"Queries":queries,"search_form":SearchReferenceForm()})