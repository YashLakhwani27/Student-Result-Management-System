"""
URL configuration for StudentResultManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from resultapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('admin-login/',adminlogin,name='adminlogin'),
    path('admin-dashboard/',admin_dashboard,name='admin_dashboard'),
    path('create_class/',create_class,name='create_class'),
    path('admin_logout/',view=admin_logout,name='admin_logout'),
    path('manage_classes/',view=manage_classes,name='manage_classes'),
    path('edit_class/<int:class_id>/',view=edit_class,name='edit_class'),
    path('create_subject/',view=create_subject,name='create_subject'),
    path('manage_subjects/',view=manage_subjects,name='manage_subjects'),
    path('edit_subject/<int:subject_id>',view=edit_subject,name='edit_subject'),
    path('add_subject_combination/',view=add_subject_combination,name='add_subject_combination'),
    path('manage_subject_combination/',view=manage_subject_combination,name='manage_subject_combination'),
    path('add_student/',view=add_student,name='add_student'),
    path('manage_students/',view=manage_students,name='manage_students'),
    path('edit_student/<int:student_id>',view=edit_student,name='edit_student'),
    path('add_notice',view=add_notice,name='add_notice'),
    path('manage_notice/',view=manage_notice,name='manage_notice'),
    path('edit_notice/<int:notice_id>/',view=edit_notice,name='edit_notice'),
    path('add_result/',view=add_result,name='add_result'),
    path('get_students_subjects/',view=get_students_subjects,name='get_students_subjects'),
    path('manage_results/',view=manage_results,name='manage_results'),
    path('edit_result/<int:stid>/',view=edit_result,name='edit_result'),
    path('change_password/',view=change_password,name='change_password'),
    path('search_result/',view=search_result,name='search_result'),
    path('check_result/',view=check_result,name='check_result'),
    path('result_page/',view=result_page,name='result_page'),
    path('notice_detail/<int:notice_id>/',view=notice_detail,name='notice_detail'),

]
