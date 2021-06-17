from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')            # Blueprint 객체를 생성할때는 이름, 모듈명, url prefix를 전달해야 함!!!

@bp.route('/hello')             # route 함수 << 애너테이션으로 매핑되는 함수
def hello_pybo() :
    return 'Hello, Pybo!'

@bp.route('/')
def index() :
    return redirect(url_for('question._list'))
