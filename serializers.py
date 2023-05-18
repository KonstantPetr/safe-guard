from pydantic import BaseModel


class CredImage(BaseModel):
    id: int
    service_name: str
    service_link: str
    login: str
    password: str
    extra: str
    misc: str
    vip: bool

    class Config:
        orm_mode = True


class CredAdd(BaseModel):
    service_name: str
    service_link: str
    login: str
    password: str
    extra: str
    misc: str
    vip: bool

    class Config:
        orm_mode = True
