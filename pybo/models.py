from flask.sessions import NullSession
from sqlalchemy.orm import backref
from pybo import create_app, db


class Question(db.Model) :
    id = db.Column(db.Integer, primary_key = True)              ## 질문 데이터의 고유 번호
    subject = db.Column(db.String(200), nullable = False)       ## 질문 제목
    content = db.Column(db.Text(), nullable = False)            ## 질문 내용
    create_date = db.Column(db.DateTime(), nullable = False)    ## 질문 작성 일시


class Answer(db.Model) :
    id = db.Column(db.Integer, primary_key = True)                                              ## 답변 데이터의 고유 번호
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))     ## 질문 데이터의 고유 번호(어떤 질문에 달린 답변인지 알기위해)
    question = db.relationship('Question', backref = db.backref('answer_set', ))                ## 답변 모델에서 질문 모델을 참조하려고 추가 --답변 모델 객체에서 질문 모델 객체의 제목을 참조(answer.question.subject)
    content = db.Column(db.Text(), nullable = False)                                            ## 답변 내용
    create_date = db.Column(db.DateTime(), nullable = False)                                    ## 답변 작성 일시


class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)                                  ## 유저 데이터의 고유 번호
    username = db.Column(db.String(150), unique = True, nullable = False)           ## 아이디
    password = db.Column(db.String(200), nullable = False)                          ## 패스워드
    email = db.Column(db.String(120), unique = True, nullable = False)              ## 이메일                  


    ## db.Integer           --- 고유 번호와 같은 숫자값에 사용
    ## db.String            --- 제목처럼 글자 수가 제한된 텍스트에 사용
    ## db.Text              --- 글 내용처럼 글자 수를 제한할 수 없는 텍스트에 사용
    ## db.DateTime          --- 날짜와 시각 표현
    ## db.ForeignKey        --- 어떤 속성을 기존 모델과 연결하기 위해 사용
    ## db.relationship      --- 기존 모델을 참조할때 사용, 참조할 모델과 역참조 설정 필요 (역참조 질문에서 답변을 참조) --- a_question(질문)에 해당하는 답변을 참조하려면 a_question.answer_set
    ## primary_key = True   --- 속성을 기본키로 지정
    ## nullable = False     --- 빈 값을 허용하지 않는다는 옵션(이 옵션을 지정하지 않으면 기본으로 빈값 허용) 
    ## ondelete = 'CASCADE' --- 연결된 질문을 삭제하면 해당 질문에 달린 답변도 삭제