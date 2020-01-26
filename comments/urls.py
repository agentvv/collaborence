from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.newComment),
    path('<int:num>/', views.viewComment),
    path('createReply/<int:num>', views.createReply),
]
