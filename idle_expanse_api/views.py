from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Star
from .serializers import StarSerializer

# Test method to return some data
@api_view(["GET"])
def getData(request):
    stars = Star.objects.all()
    serializer = StarSerializer(stars, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def addStar(request):
    serializer = StarSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
