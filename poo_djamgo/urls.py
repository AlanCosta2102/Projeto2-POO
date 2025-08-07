from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importa a view de login

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota para o login padrão do Django
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    # Suas rotas da aplicação
    path('', include('people.urls')),  
]
