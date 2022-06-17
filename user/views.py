import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import permissions, status
from .models import User, UserLog
from django.contrib.auth import login, authenticate, logout


class UserCreate(APIView):
    # 회원가입
    def post(self, request):
        user_type = request.data.get('user_type', '')
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user, created = User.objects.get_or_create(
            username=username,
        )
 
        if created:
            user.set_password(password)
            user.user_type = user_type
            user.save()
            return Response({"message": "회원가입 성공!!"}, status=status.HTTP_200_OK)
        
        return Response({"error": "이미 존재하는 계정입니다"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 회원탈퇴
    def delete(self, request):
        user = request.user
        print(f'탈퇴 user: {request.user}')
        user.delete()
        logout(request)
        print(User.objects.values('username'))
        return Response({"message":"회원탈퇴 성공!!"}, status=status.HTTP_200_OK)
    
    
class UserView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            now = datetime.datetime.now()
            UserLog.objects.create(user=user, log_date=now.strftime('%Y-%m-%d'))
            return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)
   
        return Response({"error": "username 혹은 password를 확인해주세요"}, status=status.HTTP_400_BAD_REQUEST)
    
    # 로그아웃
    def delete(self, request):
        user = request.user
        print(f'로그아웃할 user: {request.user}')
        if user:
            request.session.flush()
            return Response({"message":"로그아웃 성공!!"}, status=status.HTTP_200_OK)  
        print("됐당")
        return Response({"error":"로그인을 해주세요"}, status=status.HTTP_400_BAD_REQUEST)
    




# permission_classes = [permissions.AllowAny]
# class UserCreate(APIView):
#     # 회원가입
#     def post(self, request):
#         user_type = request.data.get('user_type', '')
#         username = request.data.get('username', '')
#         password = request.data.get('password', '')
#         print(f'username: {username}')
        
#         user = User.objects.get(username=username)
#         print(f'user: {user}')
        
#         if user:
#             return Response({"error": "이미 존재하는 계정입니다"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # user.username=username
#             # user.password=password
#             User(user_type=user_type, username=username, password=make_password(password))
#             return Response({"message": "회원가입 성공!!"}, status=status.HTTP_200_OK)

            
