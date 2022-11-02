from sqlalchemy import Column,Integer,String,Text,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Question(Base):
    #  __tablename__은 모델에 의해 관리되는 테이블의 이름
    __tablename__="question"
    # Question 모델은 고유 번호(id), 제목(subject), 내용(content), 작성일시(create_date) 속성으로 구성
    id = Column(Integer , primary_key = True)
    subject = Column(String , nullable = False)
    content = Column(Text , nullable = False)
    create_date = Column(DateTime , nullable = False)

class Answer(Base):
    __tablename__="answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable = False)
    create_date = Column(DateTime, nullable = False)
    question_id = Column(Integer,ForeignKey("question.id"))
    question = relationship("Question",backref="answers")
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer,primary_key=True)
    username = Column(String, unique =True , nullable = False)
    password = Column(String,  nullable = False)
    email = Column(String,unique=True,nullable=False)
    
