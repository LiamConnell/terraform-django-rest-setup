from rest_framework.views import APIView
from rest_framework.response import Response
import json


class BasicResponse(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        return Response(['sdf','dfg'])

    def post(self, request, format=None):
        body = request.body
        j = json.loads(body)

        return Response(j)
