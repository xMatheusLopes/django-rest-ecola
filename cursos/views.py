from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.mail import send_mail
from django.template import loader

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
            return Response(serializer.data)
        else:
            self.pagination_class.page_size = 1
            avaliacoes = Avaliacao.objects.filter(curso_id=pk)
            page = self.paginate_queryset(avaliacoes)

            if page is not None:
                serializer = AvaliacaoSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class EnviarEmail(APIView):
    def get(self, request):
        html_message = loader.render_to_string(
            'email.html', {
                'user_name': 'Matheus',
                'subject': 'Teste'
            }
        )

        send_mail(
            'Teste',
            '',
            'matheushl1996@gmail.com',
            ['corinthiano.matheus@hotmail.com'],
            fail_silently=False,
            html_message=html_message
        )
        return Response('ok', status=status.HTTP_200_OK)





