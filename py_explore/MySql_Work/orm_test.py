from sqlalchemy import create_engine 
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence

engine = create_engine('mysql+mysqldb://root:welcome123@localhost:5432/lbc_db', echo=True)

metadata = MetaData()
users = Table('users', metadata, \
                Column('id', Integer, Sequence('user_id_seq'), primary_key=True), \
                Column('name', String),
                Column('fullname', String), )

metadata.create_all(engine)

from sqlalchemy.ext.declarative import declarative_base 
Base = declarative_base()
class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title=Column('title', String(32))

from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(bind=engine)
sesh = Session()
sesh.query(Books).all()

print( Books.id, Books.title)


