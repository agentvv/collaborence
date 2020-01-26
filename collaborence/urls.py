"""collaborence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from home import views as homeViews
from courses import views as courseViews

urlpatterns = [
    path('', homeViews.index),
    path('home/', homeViews.home),
    path('register/', include('register.urls')),
    path('slides/', include('slides.urls')),
    path('schools/', courseViews.schools),
    path('comments/', include('comments.urls')),
    path('schools/<int:num>/', courseViews.school),
    path('departments/<int:num>', courseViews.department),
    path('add/<int:num>', courseViews.add),
    path('courses/<int:num>', courseViews.course),
    path('courses/createCourse/', courseViews.createCourse),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
] 
