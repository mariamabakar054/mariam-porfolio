from django.urls import path
from . import views

urlpatterns = [
    path('',              views.index,       name='index'),
    path('contact/',      views.contact,     name='contact'),
    path('connexion/',    views.login_view,  name='login'),
    path('deconnexion/',  views.logout_view, name='logout'),
    path('dashboard/',    views.dashboard,   name='dashboard'),
    path('dashboard/lu/<int:pk>/', views.mark_read, name='mark_read'),
]
