from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///dbData.sqlite', echo = True)
meta = MetaData()

Data = Table(
   'Data', meta, 
   Column('user', String), 
   Column('website', String), 
   Column('name', String),
   Column('password', String),
)
meta.create_all(engine)