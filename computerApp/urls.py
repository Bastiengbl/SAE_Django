from django.urls import path 
from . import views 
urlpatterns = [
      path('', views.index, name='index'),
      path('machines/', views.machine_list_view, name='machines'),
      path('persos/', views.personnes_list_view, name='persos'),
      path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
      path('personne/<pk>', views.personnes_detail_view, name='persos-detail'),
      path('add-machine', views.machine_add_form, name='add-machine'),
      path('about/', views.about, name='contact'),
]