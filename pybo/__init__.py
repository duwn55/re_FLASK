from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


import config

## 전역변수 db, migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()


def create_app() :              # create_app 함수가 application factory!!!
    app = Flask(__name__)
    app.config.from_object(config)          ## config.py에서 작성한 항목을 app.config 환경 변수로 부르기 위해 추가


    # ORM
    db.init_app(app)            ## 초기화
    migrate.init_app(app, db)   ## 초기화
    from . import models


    # Blueprint
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)


    # filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
 

    return app