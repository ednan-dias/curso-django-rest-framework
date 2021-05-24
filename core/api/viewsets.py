from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', '^endereco__linha1']
    # lookup_field = "nome"

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': request.data['nome']})

    # def destroy(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def retrieve(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def update(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def partial_update(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # @action(methods=['post, get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     return Response({'Hello': request.data['nome']})

    # @action(methods=['get'], detail=False)
    # def teste(self, request):
    #     return Response({'Hehe': True})
