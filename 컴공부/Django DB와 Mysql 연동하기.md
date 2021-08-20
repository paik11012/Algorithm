## Django DB와 Mysql 연동하기



1. mysql workbench 다운로드

https://www.mysql.com/products/workbench/

2. django 설정 확인하기

backend-angle폴더 내 settings.py

```python
DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', # mysql 엔진 설정 
'NAME':'anglehack', # 데이터베이스 이름 
'USER':'root', # 데이터베이스 연결시 사용할 유저 이름 
'PASSWORD':'mjmj', # 유저 패스워드 
'HOST':'localhost', 
'PORT':'3306' } }
```

여기서 name(데이터베이스 이름)과 password(내가 설정한 데이터베이스 연결 시 패스워드) 그대로 입력하기



3. mysql workbench 열은 후 쿼리문에 입력 후 실행(번개 표시)

```sql
create database anglehack
```

뒤에 anglehack는 settings.py에서 입력한 데이터베이스 이름



4. 장고에서 가상환경 만들고 실행

requirements.txt 설치

```python
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```



5. 장고에서 db 마이그레이션

```python
python manage.py makemigrations
python manage.py migrate
```

확인하면 workbench에 테이블 생성됨