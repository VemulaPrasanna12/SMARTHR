from django.contrib import admin
from app1.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','designation','joining_date','department','annual_ctc','experience']



admin.site.register(Employee,EmployeeAdmin)

