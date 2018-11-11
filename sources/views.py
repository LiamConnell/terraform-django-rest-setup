from rest_framework.views import APIView
from rest_framework.response import Response
import json

import wikipedia as wiki


class BasicResponse(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response(['sdf','dfg'])

    def post(self, request, format=None):
        data = request.data
        resp = {}
        for query in data['search']:
            resp[query] = wiki.search(query)
        return Response(resp)
