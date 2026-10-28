# from django import forms

# class ContactForm(forms.Form):
#     EmpFullName=forms.CharField(max_length=100)
#     EmpID=forms.EmailField()
#     designation = forms.CharField(max_length=100)
#     joining_date = forms.DateField()
#     department = forms.CharField(max_length=100)
#     annual_ctc = forms.DecimalField(max_digits=12, decimal_places=2)
#     experience = forms.DecimalField(max_digits=4, decimal_places=1)

from django import forms
from app1.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'