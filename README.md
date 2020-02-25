# Starting django project


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


## Starting a development server
manage.py 경로에서 실행한다
```
python manage.py runserver
```

