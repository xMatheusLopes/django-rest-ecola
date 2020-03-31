from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoViewSet,
    AvaliacaoViewSet
)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/<int:pk>/avaliacoes/<int:avaliacao_pk>/',
         CursoViewSet.as_view( { 'get': 'avaliacoes' } ),
         name='curso_avaliacao'),
]
