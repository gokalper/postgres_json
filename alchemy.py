from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy import Table, MetaData, String
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
import json
from sqlalchemy import func, cast


table_name = 'json_table7'
Base = declarative_base()


user_table = Table(table_name, MetaData(),
                   Column('id', Integer, primary_key=True),
                   Column('name', Text),
                   Column('email', Text),
                   Column('data', MutableDict.as_mutable(JSONB))
                   )


class User(Base):
    __tablename__: str = table_name
    id: int = Column(Integer, primary_key=True)
    name: str = Column(Text)
    email: str = Column(Text)
    data: json = Column(MutableDict.as_mutable(JSONB))


connection_string = 'postgresql://postgres:daycare@localhost:5432/test'
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

# ---------------------------------

try:

    result = s.query().update(table_name).where(name=john.name).values(func.jsonb_set(table_name.c.data, '{snacks}', cast("oranges", JSONB)))

    # s.commit()
    # getall = s.query('')
    print(result)

except SQLAlchemyError as e:
    print(e)


# john.update().where()

# ---------------------------------

# john.data['snacks'] = 'cookies'
# flag_modified(john, "data")
# s.add(john)
# s.commit()

# ---------------------------------


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

# ---------------------------------
