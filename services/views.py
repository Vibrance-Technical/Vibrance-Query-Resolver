from .forms import *
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
class QueryDetailView(LoginRequiredMixin,generic.DetailView):
    model = Query
    template_name = "services/ViewQuery.html"
    slug_fiel = Query.slug
    fields = ['__all__']
# Function Based Views
def home(request):
    search_reference = SearchReferenceForm(request.GET)
    queries = None
    if search_reference.is_valid():
        search_term = str(request.GET.get("slug"))
        print(search_term)
        queries = Query.objects.filter(slug = search_term)
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

@login_required
def approve_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST":
        query.status = "Approved"
        query.save()
        messages.success(request,"Approved Query successfully")
        # approval_mail(query)
        return redirect("home")
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)
@login_required
def reject_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST":
        query.status = "Rejected"
        query.save()
        messages.success(request,"Rejected Query successfully")
        # approval_mail(query)
        return redirect("home")
    else:
        messages.error(request,"Error Processing Request")
        return redirect("query_detail_view",pk = pk,slug = slug)