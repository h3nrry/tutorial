from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships, backref
from sqlalchemy import Table

Base = declarative_base()

student_course_table = Table('student_course_association', Base.metadata,
                             Column('student_id', Integer, ForeignKey('student_id')),
                             Column('course_id',  Integer, ForeignKey('courses.id')))

class Mobile(Base):
  __tablename__ = 'mobiles'

  id = Column(Integer, primary_key = True)
  number = Column(String(16))
  student_id = Column(Integer, ForeignKey('student_id'))

  def __repr__(self):
      return '<Mobile %r>' %self.number

class Student(Base):
  __tablename__ = 'students'
  id = Column(Integer, primary_key = True)
  name = Column(String(32))

  courses = relationship("CourseInfo", secondary=student_course_table, backref="students")
  mobiles = relationships("Mobile", backref="student")

  def __repr__(self):
      return '<Student %r>' %self.name

class ClassInfo(Base):
  __tablename__ = 'classes'
  id = Column(Integer, primary_key= True)
  class_name = Column(String[32])
  teacher_name = Column(String[32])
  courses = relationships("CourseInfo", backref="class_info")

  def __ref__(self):
      return '<Class %r>' %self.teacher_name

class CourseInfo(Base):
  __tablename__ = 'courses'
  id = Column(Integer, primary_key = True)
  course_name = Column(String[32])
  class_id = Column(Integer, ForeignKey('clases.id'))

  def __ref__(self):
      return '<Course %r>' %self.course_name
