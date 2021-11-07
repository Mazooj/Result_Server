from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, inspect
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR

engine = create_engine('mysql+pymysql://root:Mazooz#1@localhost/student_info')
meta = MetaData()
conn = engine.connect()


stuinfos = Table(
    'stuinfos', meta,
    Column('index', Integer, primary_key=True, autoincrement=True),
    Column('stu_name', String(255)),
    Column('roll_no', Integer, unique=True),
    Column('phone',VARCHAR(255)),
    Column('email', String(50)),
    Column('gender', String(7)),
    Column('marks_english', Integer),
    Column('marks_science', Integer),
    Column('marks_sst', Integer),
    Column('marks_maths', Integer),
    Column('marks_hindsans', Integer),
    Column('marks_marathi', Integer),
    Column('total_marks', Integer),
    Column('percentage', Integer),
    Column('result', Integer),
)
