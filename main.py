from typing import Union

from fastapi import FastAPI, File, Form, Query,UploadFile
from enum import Enum
from pydantic import BaseModel

class Schema1(BaseModel):
    name : str 
    roll_no : int 
    mob_no : int | None = None
    price : float
    tax: float | None = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"



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

# ============QUERY PARAMETER===================


@app.get("/query")
def query_fun(name:str ,usn:Union[str,None]=Query(default =None, min_length=3,max_length=4)):
    var = {"name": name,"usn":usn}
    return (var)


# @app.get("/class/{detail}")
# def enum1(detail:Detail):
#     return (detail)




@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name.value == "alexnet":
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}



    # BASEMODEL=======================


@app.post("/demo/main")
def create_item(item:Schema1):
    return item


@app.post("/form")
def form(name:str = Form() , paasword :int =Form()):
    return {"name": name , "paasword" : paasword}


@app.post("/form/")
def form1(name : Schema1):
    print("faris")
    return name

# =============file upload===========
@app.post("/file/size")
def file_length(file:bytes = File()):
    return {"file_size":len(file)}

# ==========UPLOAD FILE ===================

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.seek(0)}