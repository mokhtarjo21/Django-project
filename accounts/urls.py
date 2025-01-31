from django.urls import path
from . import views

urlpatterns = [
    path('Relay', views.Relay, name='Relay'),
    path('Signup', views.Signup, name='Signup'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
    path('EditProfile', views.EditProfile, name='EditProfile'),
    path('EditDealerProfile', views.EditDealerProfile, name='EditDealerProfile'),
    path('Balance', views.Balance, name='Balance'),
    path('ViewProfile/<int:user_id>', views.ViewProfile, name='ViewProfile'),
    path('ViewDealerProfile/<int:user_id>', views.ViewDealerProfile, name='ViewDealerProfile'),

]
