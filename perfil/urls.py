from django.urls import path 
from . import views

# informa quais links vao ser passados para url do projeto
# url redireciona o usuário para uma views
urlpatterns = [
# No campo 'views.home' indica que o nome da função que terá na views, será home
    path('home/', views.home, name='home'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('cadastrar_banco/', views.cadastrar_banco, name='cadastrar_banco'),
    path('deletar_banco/<int:id>', views.deletar_banco, name='deletar_banco'),
    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('update_categoria/<int:id>', views.update_categoria, name='update_categoria'),
]

