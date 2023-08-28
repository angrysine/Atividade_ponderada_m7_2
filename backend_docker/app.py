from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import jwt
from sqlalchemy import text

app = FastAPI()

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
engine = create_engine('postgresql://postgres:example@0.0.0:5432/postgres')



with engine.connect() as conn:
    result = conn.execute(text("create table if not exists tasks (id serial primary key, task_name varchar(255) not null, long_description varchar(255) not null, short_description varchar(50) not null,task_end_date date,task_start_date,link varchar(100) );"))
    print(result.all())

@app.get("/")
def read_root():
    return {"Hello": "World"}

