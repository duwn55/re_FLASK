import os


BASE_DIR = os.path.dirname(__file__)

## SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소
## BASE_DIR 은 프로젝트의 루트 디렉터리 (C:\reproject\flask_study)
## pybo.db라는 데이터베이스 파일을 루트 디렉터리에 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))          

## SQLALCHEMY_TRACK_MODIFICATION는 SQLAlchemy의 이벤트 처리 함수지만 파이보에서 필요하지 않아 비활성.
SQLALCHEMY_TRACK_MODIFICATION = False 

SECRET_KEY = "dev"
