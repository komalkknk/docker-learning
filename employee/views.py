from django.shortcuts import *
from .models import Employee
from .forms import EmployeeForm

def home(r): return render(r,'employee/list.html',{'employees':Employee.objects.all()})
def add(r):
 f=EmployeeForm(r.POST or None)
 if r.method=='POST' and f.is_valid(): f.save(); return redirect('/')
 return render(r,'employee/form.html',{'form':f})
def edit(r,id):
 e=get_object_or_404(Employee,id=id);f=EmployeeForm(r.POST or None,instance=e)
 if r.method=='POST' and f.is_valid(): f.save(); return redirect('/')
 return render(r,'employee/form.html',{'form':f})
def delete(r,id): get_object_or_404(Employee,id=id).delete(); return redirect('/')