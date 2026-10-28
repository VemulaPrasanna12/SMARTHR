"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homeview),
    path('emp/', views.empview),
    path('emp2/', views.emp2view),
    path('hrmanager/', views.hrmanagerview),

    path('login/', views.loginview),
    path('hrmanager/addemployee/', views.addemployeeview),
    path('hrsection/', views.hrsectionview),
    path('viewemployee/', views.viewemployeeview),
    path('addemployee/', views.addemployeeview),
    path('employee/', views.employeeview),
    path('hrmanager/viewemployee/', views.viewemployeeview),    
    path('hrmanager/addlatestnews/', views.addlatestnewsview),
    path('hrmanager/jobopenings/', views.jobopeningsview),    
    path('hrmanager/calendar/', views.calendarview),
    path('update/<int:id>', views.updateview),
    path('delete/<int:id>', views.deleteview),
    path('download/', views.download_csv),
    path('holidaycalendar/news/', views.newsview),
    # path('employee/latestnews/', views.latestnewsview),
    path('calender/', views.calendarview, name='calendarview'),
    path('holidaycalendar/', views.holidaycalendar, name='holidaycalendar'), 
    path('adddetails/', views.adddetailsview, name='add_details'),
    path('details/<int:id>/', views.detailsview, name='details'),
    path('employee/latestnews/',views.addlatestnewsview,name='addlatestnews'),
    path('employee/calendarholidays/',views.calendarview,name='calendar'),
    path('hrmanager/jobopenings/', views.jobopeningsview, name='jobopenings'),
    
    # path('hrmanager/employeedata/', views.employeedataview),

]
