from django.shortcuts import render
from .models import Areas
from .models import MetricDetails
from .models import Announcements
from django.conf import settings
from django.db import connection
from .forms import PostcodeForm

# Create your views here.
    
def index(request):
    context = {
        'settings': settings,
    }
    return render(request, 'index.html',context)
 
def base(request):
    context = {
        'settings': settings,
    }
    return render(request, 'base.html',context)
    
def report(request):
    context = {
    'settings': settings,
    }
    return render(request, 'report.html',context) 

def area_list(request):
    # Retrieve all Area objects from the covid19 database
    areas = Areas.objects.all()
    return render(request, 'area_list.html', {'areas': areas})   
    
def metricDetails_list(request):
    # Retrieve all MetricDetails objects from the covid19 database
    metrics = MetricDetails.objects.all()
    return render(request, 'metricDetails_list.html', {'metrics': metrics})   
    
def about(request):
    return render(request, 'about.html')
    
def query_view(request):
    if request.method == 'POST':
        form = PostcodeForm(request.POST)
        if form.is_valid():
            postcode = form.cleaned_data['postcode']
            # Perform the SQL query using Django's ORM
            results = MetricDetails.objects.filter(metric_name=postcode)
            #results = MetricDetails.objects.all()
            # Pass the results to the template
            return render(request, 'results.html', {'results': results})
    else:
        form = PostcodeForm()
    return render(request, 'query.html', {'form': form})
    
def results(request):
    return render(request, 'results.html')   
    
def announcements_list(request):
    announce = Announcements.objects.all()
    return render(request,'announcements.html',{'announcements':announce})
  
