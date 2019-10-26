from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import create_engine, MetaData
import json


Base = declarative_base()

class User(Base):
    __tablename__ = 'jsontable5'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    data = Column(MutableDict.as_mutable(JSONB))


connection_string = 'postgresql://postgres:password@localhost:5432/test'
db = create_engine(connection_string)

engine = db.connect()
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

some_data ={
    'snacks': "carrots",
    'bathroom': "never"
}

s = session()
john = User(id=0,
            name='John',
            email="John@domain.com",
            data=some_data
            )

# s.add(john)
# s.commit()


john.data['snacks'] = 'cookies'
flag_modified(john, "data")
s.add(john)
s.commit()

# meta = MetaData(engine)
# result = engine.execute("SELECT 1")
# print(result.rowcount)
#
# # CREATE TABLE
#
# j_table = sqlalchemy.Table("jsontable2", meta,
#                 Column('id', Integer),
#                 Column('name', Text),
#                 Column('email', Text),
#                 Column('doc', JSONB))
# meta.create_all()

# --