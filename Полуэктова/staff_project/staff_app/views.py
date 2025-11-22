from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'staff_app/add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'staff_app/employee_list.html', {'employees': employees})

def schedule(request):
    return render(request, 'staff_app/schedule.html')