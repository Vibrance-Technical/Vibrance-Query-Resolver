from .forms import *
from .filters import *
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
    if request.user.is_authenticated():
        return redirect("view_all_queries")
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
def view_all_queries(request):
    queries = QueryFilter(request.GET,queryset = Query.objects.all().order_by('-date_of_creation'))
    pending_count = Query.objects.filter(status = "Processing Query").count()
    Resolved_count = Query.objects.filter(status = "Resolved").count()
    rejected_count = Query.objects.filter(status = "Rejected").count()
    return render(request,'services/view_all_queries.html',{"Queries":queries,"Pending_Count":pending_count,"Resolved_Count":Resolved_count,"Rejected_Count":rejected_count,})

@login_required
def approve_query(request,pk,slug):
    query = Query.objects.get(id = pk,slug = slug)
    if request.method == "POST":
        query.status = "Resolved"
        query.save()
        messages.success(request,"Resolved Query successfully")
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