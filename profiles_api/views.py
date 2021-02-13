from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ TEST API VIEW """

    def get(self, request, format=None):
        """ returns a list of api view features"""

        an_apiview = [
            'Gives you most control over your logic',
        ]

        return Response({'message' : 'Hello!','an_apiview': an_apiview})
