from rest_framework.views import APIView
from rest_framework.response import Response

class HellApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIview faetures"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives yor the most contor over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'massage':'Hello!', 'an_apiview': an_apiview})
