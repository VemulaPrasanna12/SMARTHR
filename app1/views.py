from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from app1.models import Employee ,Details ,Calendar, JobOpening 
from app1.forms import EmployeeForm 
from django.http import HttpResponse
import csv

# Create your views here.

def homeview(request):
    return render(request,'app1/home.html')

@login_required
def empview(request):
    return render(request,'app1/emp.html')

def emp2view(request):
    return render(request,'app1/emp2.html')

def hrmanagerview(request):
    return render(request,'app1/hrmanager.html')

def newsview(request):
    return render(request,'app1/news.html')

def latestnewsview(request):
    return render(request,'app1/latestnews.html')

def calendarview(request):
    return render(request,'app1/calendar.html')

def loginview(request):
    return render(request,'app1/login.html')

def hrsectionview(request):
    return render(request,'app1/hrsection.html')

def addlatestnewsview(request):
    data=Details.objects.all()

    return render(request, 'app1/addlatestnews.html',{'e':data})

def viewemployeeview(request):
    data=Employee.objects.all()
    return render(request,'app1/viewemployee.html',{'e':data})

def employeeview(request):
    return render(request,'app1/employee.html')

def adddetailsview(request):
    if request.method == 'POST':
        text = request.POST.get('details', '').strip()

        if text:
            data = Details.objects.create(details=text)
            return redirect('details', id=data.id)

    return render(request, 'app1/addlatestnews.html')


# Display details by ID
def detailsview(request, id):
    data = get_object_or_404(Details, id=id)
    return render(request, 'app1/details.html', {'e': data})




def calendarview(request):
    return render(request,'app1/calendar.html')

# def jobopeningsview(request):
#     return render(request,'app1/jobopenings.html')

# def job_openings(request):
#     jobs = JobOpening.objects.all()

#     return render(
#         request,
#         'app1/job_openings.html',
#         {'jobs': jobs}
#     )


def deleteview(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/viewemployee')

def updateview(request, id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
            form=EmployeeForm(request.POST,instance=emp)
            if form.is_valid():
                form.save()
                return redirect('/viewemployee')
    return render(request,'app1/update.html',{'e': emp})    

def download_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="employeeslist.csv"'
    employees=Employee.objects.all()
    Writer =csv.writer(response)
    Writer.writerow(['emp_name','emp_id','designation','joining_date','department','annual_ctc','experience',''])
    for employee in employees:
        Writer.writerow(['emp_name,emp_id,designation,joining_date,department,annual_ctc,experience'])
    return response    


def addemployeeview(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewemployee')
    return render(request,'app1/addemployee.html',{'form':form})    


def calendarview(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        occasion = request.POST.get('occasion')

        Calendar.objects.create(
            date=date,
            occasion=occasion
        )

        return redirect('holidaycalendar')
    return render(request, 'app1/calendar.html')


def holidaycalendar(request):
    holidays = Calendar.objects.all().order_by('date')

    return render(
        request,
        'app1/holidaycalendar.html',
        {'holidays': holidays}
    )


# def jobopening(request):
#     if request.method == 'POST':
#         JobOpening.objects.create(
#             role=request.POST.get('role'),
#             exp=request.POST.get('exp'),
#             skills=request.POST.get('skills'),
#             ctc=request.POST.get('ctc'),
#             notice=request.POST.get('notice')
#         )

#         return redirect('jobopenings')

#     return redirect('jobopenings')


def jobopeningsview(request):
    return render(request, 'app1/jobopenings.html')