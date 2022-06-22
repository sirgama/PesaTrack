from django.shortcuts import render

# Create your views here.
def landing(request):
    
    return render(request, 'dashboard/landing.html')


def dashboard(request):
    current_user = request.user
    context = {
        'current_user':current_user
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def expenses(request):
    current_user = request.user
    context = {
        'current_user':current_user
    }
    
    return render(request, 'dashboard/expenses.html', context)