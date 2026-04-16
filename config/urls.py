"""
URL configuration for config project.

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
from jobs.views import create_job, job_status, dashboard, all_jobs, delete_all_jobs

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', dashboard),
    path('dashboard/', dashboard),
    path('api/job/', create_job),
    path('api/job/<int:job_id>/', job_status),
    path('api/jobs/', all_jobs),
    path('api/delete-all/', delete_all_jobs),
]
