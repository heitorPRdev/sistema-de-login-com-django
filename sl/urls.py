from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro,name='cadastro'),
    path('login/', views.loginP,name='login'),
    path('sucesso/',views.sucesso,name='sucesso')
]