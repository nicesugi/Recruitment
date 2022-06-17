from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# 지원자(candidate), 채용 담당자(recruiter) 등 유저 타입을 저장
class UserType(models.Model):
    POSITION = (
        ('C', 'candidate'),
        ('R', 'recruiter'),
    )

    user_type = models.CharField(max_length=10, choices=POSITION)


class User(AbstractBaseUser):
    user_type = models.ForeignKey(to=UserType, on_delete=models.CASCADE)
    username = models.CharField("사용자 계정", max_length=20)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=256)
    fullname = models.CharField("이름", max_length=20)

    # is_active가 False일 경우 계정이 비활성화됨
    is_active = models.BooleanField(default=True) 
    
    # id로 사용 할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용된다.
    USERNAME_FIELD = 'email'

    # user를 생성할 때 입력받은 필드 지정
    REQUIRED_FIELDS = [email]

    objects = UserManager() # custom user 생성 시 필요
    
    def __str__(self):
        return f'{self.user_type} {self.eamil}'
    
        # admin 권한 설정
    @property
    def is_staff(self): 
        return self.is_admin
 
    
# 유저가 마지막으로 로그인한 날짜(Date)와 마지막으로 지원한날짜
class UserLog(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    log_date = models.DateField("최근 로그인")
    last_application = models.DateField("마지막 지원일자")
    
    def __str__(self):
        return f'{self.user}님의 {self.log_date} {self.last_application}'
