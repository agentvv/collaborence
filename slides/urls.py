from django.urls import path

from . import views

urlpatterns = [
    path('<int:num>/<int:page>', views.view, name='view'),
    path('upload/<int:num>', views.uploadSlide, name='upload'),
]
