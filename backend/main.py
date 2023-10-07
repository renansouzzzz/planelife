from fastapi import FastAPI, status

from backend.schemas.user import UserCreate, UserUpdate
from backend.schemas.user_adm import UserAdmCreate, UserAdmUpdate

from .config.database import Base, engine
from .repository import user_repository, user_adm_repository

app = FastAPI(
    title="PlaneLife API",
    description="API > ReactNative",
    openapi_url="/api/v1/"
)

Base.metadata.create_all(engine)

@app.get("/users", tags=['User'])
def get_user():
        return user_repository.get()

@app.post("/users/create", status_code=status.HTTP_201_CREATED, tags=['User'])
def create_user(payload: UserCreate):
        return user_repository.create(payload)

@app.put("/users/update/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['User'])
def update_user(user: UserUpdate, id: int):
        return user_repository.update(user, id)

@app.delete('/users/delete/{id}', tags=['User'])
def delete_user(id: int):       
        return user_repository.delete(id)


# user adm --------------------------------------

@app.get("/users-adm", tags=['UserAdm'])
def get_user_adm():
        return user_adm_repository.get()

@app.post("/users-adm/create", status_code=status.HTTP_201_CREATED, tags=['UserAdm'])
def create_user_adm(payload: UserAdmCreate):
        return user_adm_repository.create(payload)

@app.put("/users-adm/update/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['UserAdm'])
def update_user_adm(user: UserAdmUpdate, id: int):
        return user_adm_repository.update(user, id)

@app.delete('/users-adm/delete/{id}', tags=['UserAdm'])
def delete_user_adm(id: int):       
        return user_adm_repository.delete(id)