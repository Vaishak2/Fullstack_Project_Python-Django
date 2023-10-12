
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    # path('', views.home, name='home'),
    path('medicine_list', views.medicine_list, name='medicine_list'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('search_bar', views.search_bar, name='search_bar'),
    path('doctors', views.doc_list, name='doctors'),
    path('contact', views.contact, name='contact'),

    path('medicine_detail/<int:pk>',login_required(views.MedicineDetailView.as_view()), name='medicine_detail'),
    path('medicine_list/create/', login_required(views.MedicineCreate.as_view()), name='med_create'),
    path('medicine_detail/update/<int:pk>',login_required(views.MedicineUpdate.as_view()), name='med_update'),
    path('medicine_detail/delete/<int:pk>', login_required(views.MedicineDelete.as_view()), name='med_delete'),
    
    
]