from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import jwt
import json
from sqlalchemy import text
from datetime import date
from fastapi.security import OAuth2PasswordBearer



app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "secret"
origins = [
    "http://localhost:3000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#dialect[+driver]://user:password@host/dbname[?key=value..]
engine = create_engine('postgresql://postgres:example@db:5432/postgres')




with engine.connect() as conn:
    result = conn.execute(text("create table if not exists tasks (id serial primary key, task_name varchar(255) not null, long_description varchar(255) not null, short_description varchar(50) not null,task_end_date date,task_start_date date,link varchar(100) );"))
    result2 = conn.execute(text("create table if not exists users (id serial primary key, username varchar(255) not null, password varchar(255) not null);"))
    conn.commit()


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/register")
def register(credentials: dict):
    username = credentials["username"]
    password = credentials["password"]

    with engine.connect() as conn:
        result = conn.execute(text(f"select * from users where username = '{username}';"))
        user = result.first()
        if user is not None:
            raise HTTPException(status_code=401, detail="User already exists")
        
        result = conn.execute(text(f"insert into users (username, password) values ('{username}', '{password}');"))
        conn.commit()
        return {"status": "ok"}

@app.post("/login")
def login(credentials: dict):
    
    username = credentials["username"]
    password = credentials["password"]

    with engine.connect() as conn:
        result = conn.execute(text(f"select * from users where username = '{username}' and password = '{password}';"))
        
        user = result.first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid user/password combination")
        
        payload = {
            "username": username,
            "password": password
        }
        token = jwt.encode(payload, SECRET_KEY)
        return {"token": token, "token_type": "bearer"}

@app.get("/tasks",)
def get_tasks(dict:dict = Depends(verify_token)):
    
    with engine.connect() as conn:
        result = conn.execute(text("select * from tasks;"))
     
        l = []
        for row in result:
            l.append(row)

        return str(l)
        # return [dict(row) for row in result]
    
@app.post("/tasks")
def create_task(dict: dict,a= Depends(verify_token)):
    task_name = dict["task_name"]
    long_description = dict["long_description"]
    short_description = dict["short_description"]
    task_end_date = dict["task_end_date"]
    task_start_date = dict["task_start_date"]
    link = dict["link"]

    try:
        with engine.connect() as conn:
            result = conn.execute(text(f" insert into tasks (task_name, long_description, short_description, task_end_date, task_start_date, link) values ('{task_name}', '{long_description}', '{short_description}', '{task_end_date}', '{task_start_date}', '{link}');"))
            conn.commit()
            return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "error": str(e),"task_name":task_name}
    
# @app.delete("/tasks/")
# def delete_task(id: int= Depends(verify_token)):
#     with engine.connect() as conn:
#         result = conn.execute(text("delete from tasks where id = :id;"), id=id)
#         conn.commit()
#         return {"status": "ok"}
    
@app.get("/tasks_date/")
def get_task(dict:dict ,a=Depends(verify_token)):
    lista =dict["date"].split("/")
    _date = date(int(lista[2]),int(lista[1]),int(lista[0]))
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from tasks where cast(task_end_date as date)= cast('{dict['date']}' as date);"))
        
        l = []
        for row in result:
            l.append(row)
        
        return str(l)

@app.get("/check_token")
def check_token(dict:dict = Depends(verify_token)):
    return {"status": True}
