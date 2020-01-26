from django.urls import path

from . import views

urlpatterns = [
    path('<int:num>/', views.view, name='view'),
    path('upload/<int:num>', views.uploadSlide, name='upload'),
]
