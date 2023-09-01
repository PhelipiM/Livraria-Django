from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet
from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet, CompraViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autor", AutorViewSet)
router.register(r"livro", LivroViewSet)
router.register(r"compras", CompraViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
]



