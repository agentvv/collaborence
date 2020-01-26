from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('<int:num>/<int:num2>', views.newComment),
    path('viewComment/<int:num>/', views.viewComment),
    path('createReply/<int:num>', views.createReply),
]
