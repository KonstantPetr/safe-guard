import uvicorn

from fastapi import FastAPI
from typing import List

from db_engine import db
from models import Credentials
from serializers import CredImage, CredAdd

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


# # коннект с базой данных при старте прилшожения
# @app.on_event('startup')
# def startup():
#     db.connection()
#
#
# # дисконнект с базой данных при завершении приложения
# @app.on_event('shutdown')
# def shutdown():
#     db.dispatch


# получение записей из БД
@app.get('/credentials/', response_model=List[CredImage])
def show_credentials():
    image = db.query(Credentials).all()
    return image


# получение записи из БД
@app.get('/credentials/{credentials_id}', response_model=List[CredImage])
def show_credentials_item(credentials_id: int):
    image = db.get(Credentials, credentials_id)
    return image


# добавление записи в БД
@app.post('/credentials/', response_model=CredAdd)
def add_credentials(cred: CredAdd):
    print(f'cred = {cred}')
    print(f'cred.service_name = {cred.service_name}')
    print(f'cred.vip = {cred.vip}')
    item = Credentials(service_name=cred.service_name,
                       service_link=cred.service_link,
                       login=cred.login,
                       password=cred.password,
                       extra=cred.extra,
                       misc=cred.misc,
                       vip=cred.vip)
    print(f'item = {type(item)}')
    # last_record_id = db.add(item)
    db.add(item)
    db.commit()
    last_record_id = item.id
    print(f'last_record_id = {last_record_id}')
    # db.refresh(item)
    return {'message': 'success', 'id': last_record_id}


# удаление записи из БД
@app.delete('/credentials/{credentials_id}')
def delete_credentials(credentials_id: int):
    item = db.query(Credentials).filter(Credentials.id == credentials_id).first()
    db.delete(item)
    db.commit()
    return {'detail': 'Credentials successfully deleted', 'status_code': 204}


# изменение записи в БД
@app.post('/credentials/{credentials_id}', response_model=CredImage)
def add_credentials(credentials_id: int, cred: CredAdd):
    item = db.query(Credentials).filter(Credentials.id == credentials_id).first()
    db.commit()
    last_record_id = db.refresh(item)
    return {**Credentials.dict(), 'id': last_record_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
