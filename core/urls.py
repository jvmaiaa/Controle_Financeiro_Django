from django.contrib import admin
from django.urls import path, include

# o usuário acessa uma existente no projeto
# para criar uma nova rota: path('url digitada pelo usuario/', include('redirecionamento para a pasta do app.urls')),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),

]
