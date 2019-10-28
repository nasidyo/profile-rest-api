from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializer
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIview faetures"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives yor the most contor over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'massage':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response('methods', 'PUT')
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'methods','PATCH'})
    def delete (self, request, pk=None):
        """Delete an object"""
        return Response({'methods','DELETE'})

class HelloApiViewSet (viewsets.ViewSet):

    serializer_class = serializer.HelloSerializer

    """Test API ViewSet"""
    def list(self, request):
        """Return a list of APIview faetures"""
        a_viewset = [
            'Users action (list, Create, retrieve, update, partial_update)',
            'Automatically map to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'massage':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
