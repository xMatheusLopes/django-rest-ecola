from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None, avaliacao_pk=None):
        curso = self.get_object()
        if avaliacao_pk:
            serializer = AvaliacaoSerializer(curso.avaliacoes.get(pk=avaliacao_pk))
        else:
            serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


