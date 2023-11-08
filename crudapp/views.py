from django.shortcuts import render,redirect
from . models import Employee

# Create your views here.
def index(request):
    msg=""
    if request.method=='POST':
        empid=request.POST['empid']
        empname=request.POST['empname']
        empaddress=request.POST['empaddress']
        department=request.POST['department']
        salary=request.POST['salary']
        emp=Employee(empid=empid,empname=empname,empaddress=empaddress,department=department,salary=salary)
        emp.save()
        msg='Success'
    empinfo=Employee.objects.all()
    return render(request,"index.html",{'msg':msg ,'empinfo':empinfo})

def deleteemp(request,id):
    emp=Employee.objects.get(empid=id)
    emp.delete()
    return redirect("index")

def updateemp(request,id):
    emp=Employee.objects.get(empid=id)
    return render(request,"update.html",{'emp':emp})

def updatecode(request):
    if request.method=='POST':
        empid=request.POST['empid']
        empname=request.POST['empname']
        empaddress=request.POST['empaddress']
        department=request.POST['department']
        salary=request.POST['salary']
        Employee.objects.filter(empid=empid).update(empname=empname,empaddress=empaddress,department=department,salary=salary)
        return redirect("index")