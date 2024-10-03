from rest_framework import response,status,request,generics
from rest_framework.response import Response
from rest_framework.views import APIView


class DemoAPI(APIView):
    def get(self,request):
        return Response(data={"message":"Hello World...!!!!"})