from rest_framework.response import Response
from rest_framework.decorators import api_view

# Test method to return some data
@api_view(["GET"])
def getData(request):
    star = {"name": "sol", "classification": "Yellow-Dwarf"}
    return Response(star)
