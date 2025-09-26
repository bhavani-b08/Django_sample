from django.urls import path 
from . import views 
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app'
urlpatterns = [ 
    path('', views.Add_data.as_view(), name = 'home'),
    path('add/', views.Add_data.as_view() , name='add_data'),
    path('success/', views.success, name="success"),
    path('login/', LoginView.as_view() , name='login'),
    path('secret/', views.secret_page , name='secret'),
    path('logout/', LogoutView.as_view() , name='logout'),
]