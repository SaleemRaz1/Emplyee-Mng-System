from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Employee
from django.db.models import Q
# Create your views here.
def Index(request):
    return render (request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    contecxt={
        'emps':emps
    }
    return render (request,'all_emp.html',contecxt)

def add_emp(request):
    
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        dept=request.POST['dept']
        role=request.POST['role']
        
        data=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        data.save()
        return redirect('all_emp') 
        # return HttpResponse('Data Uploaded on data base')
    elif request.method=='GET':
     return render (request,'add_emp.html')
    else:
        return HttpResponse("an error Occured") 

def remove_emp(request,emp_id=0):
    if emp_id:
        
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Emplyee Removed")
        except:
            return HttpResponse("enter valid emp id")
        
    emps=Employee.objects.all()
    return render (request,'remove_emp.html',{'emps':emps})

def filter_emp(request):
    
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
         emps= emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
         
        if dept:
            emps= emps.filter(dept__name=dept)
        if role:
            emps= emps.filter(role__name=role)
            
        context={
          'emps':emps
                 }    
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
      return render (request,'filter_emp.html')
  
    else:
        return HttpResponse("An Exception Error")    
        
    

