# Starting django project


<h3 style="color:'red'">Starting a development server</h3>
manage.py 경로에서 실행한다

```
python manage.py runserver
```

<h3 style="color:'red'">Urls</h3>

admin
```
/admin
```

<h3 style="color:'red'">Connecting to UI !</h3>

install necessary package
```
pip install django-cors-headers
```

in settings.py add corsheaders, need to add middleware class to listen in on responses 
```
INSTALLED_APPS = [
    'corsheaders'
]


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True
```




## Creating a project < 프로젝트 생성 >

먼저 프로젝트를 만들 폴더를 생성한다
```
mkdir <folder name>
```

생성한 폴더 안에서 아래 명령을 실행하여 가상환경을 생성한다. 이름은 주로 venv 로 사용한다.
```
python -m venv <name> 
```
가상환경을 설치 한 후 실행한다
```
source venv/bin/active
```
가상환경을 실행 한 후 django 를 설치한다
```
python -m pip install Django
```
프로젝트를 생성한다. name은 원하는 프로젝트 이름을 고른다. 이름 뒤에 오는 . 은 프로젝트를 현재 디렉토리 안에 생성한다는 뜻이다.
```
django-admin startproject <name> .
```

## Creating an app < 앱 생성 >
manage.py 경로에서 polls 앱을 생성한다. 앱은 프로젝트안에 있다고 생각했는데 여기서는 poll 이라는 앱을 프로젝트의 상위 모듈이라고 한다며 프로젝트와 같은 경로에 poll 앱을 생성한다.
( 사실 앱을 어느 경로에 생성하던 개발자 마음인것 같음)

아래 명령어로 앱을 생성한다.
```
python manage.py startapp <name>
```

## Write your first view < View 생성하기 >
[http://127.0.0.1:8000/polls/] 라는 url 을 생성하려면 어떻게 해야하나? 

이건 poll 앱의 Home 을 얘기한다. polls/views.py 에서 index page 를 생성한다.
```
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, world. You are at the poll index')
```


polls/urls.py 에 url 를 추가한다.
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

djangoPractice/urls.py 에서 poll 앱의 url 를 추가한다.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## Connecting database (데이터베이스 초기 설정)
mysql 사용시 mysqlclient 설치 필요
```
pip install mysqlclient
```

mysql 사용시, user 이름이 root, 비밀번호가 root 인 계정으로 mysql 을 실행 하겠다는 뜻 터미널에서 아래 명령어 실행
``` 
mysql -uroot -proot
```

mysql user 생성 username : django, password: django
```
CREATE USER 'django'@'localhost' INDENTIFIED BY 'django'; 
```

유저를 생성 직후에는 아무 권한이 없다. 권한을 줘야한다.
```
GRANT ALL PRIVILEGES ON * . * TO 'django'@'localhost';
FLUSH PRIVILEGES;
```

데이터베이스 조회
```
show databases;
```

데이터베이스 생성
```
create database <name> character set utf8;
grant all privileges on django_practice.* TO django@localhost identified by 'django';
grant all privileges on django_practice.* TO django@'%' identified by 'django';

flush privileges;
```

Quit mysql and log back in with new user
```
quit
mysql -udjango -pdjango
```


데이터베이스 연결 djangoPractice/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_practice',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST':'localhost'
    }
}

```

create tables 
```
python manage.py migrate
```

check if tables are created
```
mysql -udjango -pdjango;
show databases;
use django_practice;
show tables;
```

create Models yourself (직접 테이블 생성하기) polls/models.py 참고

polls 앱을 사용할것이라고 djangoPractice/settings.py 에 선언해야 한다.


models.py 에 변경된 부분을 miragtion 으로 보관(?) 하겠다는 것이다. 
migration 정보는 polls/migrations 아래 저장되며 git에 올려서 협업하는데 사용한다(?)
데이터베이스 변경 히스토리 조작/추적 가능해서 이렇게 makemigrations/migrate 명령을 따로 두는것 같음 
```
python manage.py makemigrations
```

migrate 를 해야 변경된 부분이 데이터베이스에 반영된다.
```
python manage.py migrate
```





