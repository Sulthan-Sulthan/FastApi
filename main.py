from typing import Union

from fastapi import FastAPI

from enum import Enum

class Detail(str, Enum):
    name = "FARIS"
    roll_no = "45"
    company = "Raasoft"


app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Hello": "faris how you"}


# NORMAL===========================

@app.get("/helloooo")
def new_fun():
    return {"Hello": "this is new function"}



# PATH PARAMETER-----------------------------


@app.get("/item/{Item}")
def fun2(Item): 
    var_names = {"path variable": Item}
    return(var_names )


# PATH PARAMETER WITH TYPES===================

@app.get("/types")
def fun3(Item:int ,name: Union[float,int,None]=None):          #Union which means we can give any types which is mentioned in  the list or without value
    var_names = {"path variable": Item,"NAME":name}
    return (var_names)


@app.get("/class/{detail}")
def enum1(detail:Detail):
    return (detail)