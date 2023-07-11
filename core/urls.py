from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# dentro do parametro do include, é colocado o app e o arquivo que vai ser mostrado, quando acessarmos aquela url
# Ex: path('perfil/', include('perfil.urls')), 
# quando tiver perfil/ na barrra de pesquisa, o django vai chamar o arquivo urls do app perfil
urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)