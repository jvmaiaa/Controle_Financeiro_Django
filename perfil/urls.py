from django.urls import path 
from . import views

# informa quais links vao ser passados para url do projeto
# url redireciona o usuário para uma views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('cadastrar_banco/', views.cadastrar_banco, name='cadastrar_banco')
]

