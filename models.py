from sqlalchemy import Column, Integer, String, Boolean
from db_engine import engine, Base


class Credentials(Base):
    __tablename__ = 'credentials'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    service_name = Column(String)
    service_link = Column(String)
    login = Column(String)
    password = Column(String)
    extra = Column(String)
    misc = Column(String)
    vip = Column(Boolean)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
