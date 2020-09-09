from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('allckts/', views.allckts, name='allckts'),
    path('hadd/', views.hadd, name='halfadder'),
    path('fadd/', views.fadd, name='fulladder'),
    path('hsub/', views.hsub, name='halfsubstractor'),
    path('fsub/', views.fsub, name='fullsubstractor'),
]
