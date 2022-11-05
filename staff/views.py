from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Employee


# Create your views here.
def home(request):
    return render(request, 'home.html', {'employees': Employee.objects.all()})


def Profile(request, pk):
    staff = Employee.objects.get(id=pk)
    team = Employee.objects.filter(supervisor_id=pk)

    return render(request, 'profile.html', {"staff": staff, 'teams': team})


def Search(request):
    q = request.GET.get('search')
    results = []
    error = None

    if len(q) < 3:
        error = "Your search query must contain at least three characters."
    else:
        results = Employee.objects.filter(
            Q(name__icontains=q) |
            Q(surname__icontains=q) |
            Q(adress__icontains=q) |
            Q(phone__icontains=q) |
            Q(title__icontains=q)
        )

    return render(request, 'search.html', {
        "employees": results, 
        'q': q,
        "error": error
    })


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('home')
