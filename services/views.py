from .forms import *
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.
def home(request):
    search_reference = SearchReferenceForm(request.GET)
    queries = None
    if search_reference.is_valid():
        queries = Query.objects.filter(slug = search_reference)
    return render(request,"services/home.html",{"Queries":queries,"search_form":SearchReferenceForm()})

def create_query(request):
    if request.method == "POST":
        query_form = QueryCreateForm(request.POST,request.FILES)
        if query_form.is_valid():
            query = query_form.save(commit=False)
            query.status = "Processing Query"
            query.save()
            messages.success(request,"Successfully raised a query. You will be notified about the status soon")
            return redirect("home")
        else:
            return render(request,"services/create_query.html",{"form":query_form,"query_form_errors":query_form.errors})
    else:
        return render(request,"services/create_query.html",{"form":QueryCreateForm()})