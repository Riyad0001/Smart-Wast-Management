from django.shortcuts import render,redirect
from .models import WasteBin, CollectionSchedule, UserReport,WasteRequest,CollectionHistory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import UserReportForm,Registratin_form
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
def bin_list(request):
    search_query = request.GET.get('search', '')
    bins = WasteBin.objects.filter(location__icontains=search_query)
    return render(request, 'bin_list.html', {'bins': bins})

def schedule_list(request):
    schedules = CollectionSchedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def report_view(request):
    reports = UserReport.objects.select_related('user', 'bin').order_by('-report_date')
    
    return render(request, 'report_list.html', { 'reports': reports})
@login_required
def create_report_view(request):
    reports = UserReport.objects.select_related('user', 'bin').order_by('-report_date')
    if request.method == 'POST':
        form = UserReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  
            report.save()
            messages.success(request, 'Your report has been submitted successfully!')
            return redirect('report_list')
    else:
        form = UserReportForm()

    return render(request, 'report_form.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            messages.success(request, "Log In Successfully")
            return redirect('bin_list')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Log Out Sucessfully")
    return redirect('login')

@login_required
def user_dashboard(request):
    user_reports = UserReport.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'user_reports': user_reports})

@login_required
def waste_request(request):
    if request.method == 'POST':
        bin_id = request.POST['bin_id']
        bin = WasteBin.objects.get(id=bin_id)
        WasteRequest.objects.create(user=request.user, bin=bin)
        messages.success(request, "Your Request Sent to Admin and they contact you later")
        return redirect('user_dashboard')
    bins = WasteBin.objects.all()
    return render(request, 'wast_request.html', {'bins': bins})

@login_required
def user_profile(request):
    user_reports = UserReport.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'user_reports': user_reports})

@login_required
def collection_history(request):
    waste_bins = WasteBin.objects.filter(user=request.user)  


    history = CollectionHistory.objects.filter(bin__user=request.user)  
    
    return render(request, 'collection_history.html', {'history': history})

from django.http import JsonResponse


def waste_trends(request):
    bin_usage = WasteBin.objects.values('location').annotate(total_fill=Sum('current_fill'))
    bin_usage_list = list(bin_usage) 
    return render(request, 'waste_trends.html', {'bin_usage': bin_usage_list})

def registerForm(request):
    if request.method=="POST":
        reg_form=Registratin_form(request.POST)
        if reg_form.is_valid:
            reg_form.save(commit=True)
            messages.success(request,"Registered Successsfully!")
            return redirect('homepage')
    else:
        reg_form=Registratin_form()
    return render(request,'register.html',{'form':reg_form,'type':'Register'})

def feature_coming(request):
    return render(request,'coming.html')
def res(request):
    return render(request,'res.html')