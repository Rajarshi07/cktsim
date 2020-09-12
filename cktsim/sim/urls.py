from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('allckts/', views.allckts, name='allckts'),
    path('adder/hadd/', views.hadd, name='halfadder'),
    path('adder/fadd/', views.fadd, name='fulladder'),
    path('subtractor/hsub/', views.hsub, name='halfsubstractor'),
    path('subtractor/fsub/', views.fsub, name='fullsubstractor'),
    path('gate/and/', views.gate_and ,name='gate_and'),
    path('gate/or/', views.gate_or ,name='gate_or'),
    path('gate/xor/', views.gate_xor ,name='gate_xor'),
    path('gate/xnor/', views.gate_xnor ,name='gate_xnor'),
    path('gate/nand/', views.gate_nand ,name='gate_nand'),
    path('gate/nor/', views.gate_nor ,name='gate_nor'),
    path('gate/not/', views.gate_not ,name='gate_not'),

]
