import string
import secrets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Urls
class MapUrlAPIView(APIView):
    def post(self,request):
        print(request.data)
        key=self.creat_key()
        new_data=Urls(client_url=request.data.get('url'),mapped_key=key)
        new_data.save()
        return  Response({"message":"got url"})


    def creat_key(self):
        to_decode=string.ascii_letters + string.digits
        secret_key=''.join(secrets.choice(to_decode) for _ in range(10))
        return secret_key


class FindUrlAPIView(APIView):
    def get(self,request,key):
        print(key)
        data=Urls.objects.filter(mapped_key=key)
        print((data[0].client_url))
        return Response("got the key")

class Homepage():
    def homepage_view(request):
        return render(request, 'homepage.html')