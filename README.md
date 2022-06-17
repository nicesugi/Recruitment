# Recruitment : 미니 채용 관리 시스템 / 6월 17일 / 제한시간 1시간


- user/models.py : AbstractBaseUser 상속받아서 USERNAME_FIELD 에 email 필드로 지정해서 python manage.py createsuperuser 로 admin 유저를 만들어보세요.
- 서버 실행해서 2번에서 만든 admin email/password 으로 http://127.0.0.1:8000/admin 으로 로그인 되는지 테스트
- user/models.py 지원자(candidate), 채용 담당자(recruiter) 등 유저 타입을 저장할 수 있는 UserType모델을 만들고 User모델과 관계를 지어 보세요.
- user/views.py : rest framework의 APIView를 상속받아서 회원가입을 위한 post 메소드를 구현해보세요. 패스워드 해쉬는 아래 메소드 참고해서 작성할 것
- 포스트맨으로 회원가입 view 테스트 이후에 admin에서 확인 테스트 
- user/models.py : <유저가 마지막으로 로그인한 날짜(Date)와 마지막으로 지원한날짜>를 저장할수 있는 UserLog 라는 모델을 만들어보세요.
- user/views.py : 로그인View에서 로그인할때 현재시간으로 UserLog의 마지막로그인날짜를 저장하는 코드를 작성해보세요.
- 포스트맨으로 로그인 view 테스트  
