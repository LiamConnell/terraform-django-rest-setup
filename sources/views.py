from rest_framework.views import APIView
from rest_framework.response import Response

import os
import json
from dotenv import load_dotenv
load_dotenv(".keys")

import wikipedia as wiki
from django.shortcuts import render
import requests


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BasicResponse(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #ip = requests.get('https://api.ipify.org/').text
        is_cached = ('geodata' in request.session)

        if not is_cached:
            ip = get_client_ip(request)
            geourl = 'http://api.ipstack.com/' + ip + '?access_key=' + os.environ.get('IPSTACK_KEY') + '&format=1'
            response = requests.get(geourl)
            geodata = response.json()
            request.session['geodata'] = geodata

        geodata = request.session['geodata']

        return render(request, 'page.html', {
            'ip': geodata['ip'],
            'country': geodata['country_name'],
            'latitude': geodata['latitude'],
            'longitude': geodata['longitude'],
            'api_key': os.environ.get('GMAPS_KEY'),
            'is_chached': is_cached
        })

    def post(self, request, format=None):
        data = request.data
        resp = {}
        for query in data['search']:
            resp[query] = wiki.search(query)
        return Response(resp)
