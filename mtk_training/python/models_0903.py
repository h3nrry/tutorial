from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    phones = relationship("Phone", backref="student")

    def __str__(self):
        return self.name

class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(64))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return self.number

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import os
    dn = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dn, "data_0903.sqlite")
    engine = create_engine(fn, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    S = sessionmaker(bind=engine)
    session = S()
    # 增加新東西(phones)
    ps = [Phone(number="0912345678"),
          Phone(number="0922222222"),
          Phone(number="0917876666")]
    s = Student(name="Elwing", phones=ps)
    session.add(s)
    # 確定做完所有事情最好手動commit一次
    session.commit()
    # Query語法(for in phones)
    q = session.query(Student).filter_by(name="Elwing")
    student = q.first()
    print("找出來的學生:", student)
    for p in student.phones:
        print("學生電話:", p)
        print("所屬學生:", p.student)
