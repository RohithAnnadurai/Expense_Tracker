from django.shortcuts import render, redirect, get_object_or_404
from .models import Expenses

#home / Dashboard
def home(request):
    expenses = Expenses.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)

    return render(request, 'home.html', {'expenses':expenses, 'total_expenses': total_expenses})

# Display all expenses
def expense_list(request):
    expenses = Expenses.objects.all()

    return render(request,'expense_list.html', {'expenses': expenses})

# Add Expenses
def add_expense(request):
    if request.method == 'POST':

        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']
        description = request.POST['description']

        Expenses.objects.create(
            title=title,
            amount=amount,
            category=category,
            date=date,
            description=description
        )

        return redirect('expense_list')
    return render(request, 'add_expense.html')

# Edit expense
def edit_expense(request, id):
    expense = get_object_or_404(Expenses,id=id)

    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.description = request.POST['description']
        expense.save()

        return redirect('expense_list')
    return render(request, 'edit_expense.html', {'expense': expense})

# Delete expense
def delete_expense(request,id):
    expense = get_object_or_404(Expenses, id=id)
    expense.delete()

    return redirect('expense_list')


# Create your views here.
