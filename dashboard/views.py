from django.shortcuts import redirect, render
from .models import Expenses, Categories
from .forms import NewExpenditureForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required



# Create your views here.
def landing(request):
    
    return render(request, 'dashboard/landing.html')

@login_required
def dashboard(request):
    current_user = request.user
    expenses = Expenses.objects.filter(user=current_user).all()
    expenses.reverse()
    # query_set = self.get_queryset() 
    # context = super(FinalView, self).get_context_data(**kwargs) 
    # if query_set is not None: 
    #     context['sales'] = query_set.aggregate(Sum('sales')) 
    #     return context
    total_exp = Expenses.objects.aggregate(Sum('amount')).get('amount__sum')
    print(total_exp)
    context = {
        'total':total_exp,
        'expenses':expenses,
        'current_user':current_user
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def expenses(request):
    current_user = request.user
    expenses = Expenses.objects.filter(user=current_user).all()
    expenses.reverse()
    
    
    if request.method == 'POST':
        form = NewExpenditureForm(request.POST)
        if form.is_valid():
            Expenses.user_id = request.user
            description = form.cleaned_data.get('description')
            amount = form.cleaned_data.get('amount')
            category = form.cleaned_data.get('category')
            
            p, created = Expenses.objects.get_or_create(description=description, amount=amount, category=category, user=current_user)
            form.save(commit=False)
            return redirect('expenses')
    else:
        form = NewExpenditureForm()
        
    context = {
        'expenses':expenses,
        'current_user':current_user,
        'form':form,
    }
    
    return render(request, 'dashboard/expenses.html', context)