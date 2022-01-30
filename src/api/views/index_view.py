from rest_framework.decorators import api_view

from rest_framework.response import Response


@api_view(['GET'])
def index_view(request):
    return Response({'status': 'successful'})
