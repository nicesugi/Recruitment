from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User

class UserCreate(APIView):
    # 회원가입
    def post(self, request):

        # username = request.data.get('username', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        # fullname = request.data.get('fullname', '')

        user = authenticate(request, email=email, password=password)
        if request.data in user:
            return Response({"error": "이미 존재하는 계정입니다"}, status=status.HTTP.status)

        else:
            user = User.objects.create_user(request, email=email, password=password)
        print(f'{request.data} 의 user {user}')
        return Response({"message": "회원가입 성공!!"})
