from django.urls import path
from .import views
from med_store_api import views


urlpatterns = [
    
    path('login', views.login, name='login_api'),
    path('register', views.register.as_view()),
    path('available_med', views.available_med, name='available_med_api'),
    path('search_med', views.search_med, name='search_med'),
    
    path('user_details/<int:pk>', views.user_details.as_view()),
    path('medicine_details/<int:pk>', views.medicine_details.as_view()),
    path('add_medicine', views.add_medicine.as_view()),
]


    # path('welcome', views.welcome.as_view(), name='welcome_api'),
    # path('simpleapi', views.simpleapi, name='simple_api'),