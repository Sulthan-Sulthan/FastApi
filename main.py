from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, File, Form, HTTPException, Query,UploadFile,Request
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


# +++++
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
    return {"filename": file}

@app.post("/file_name/")
async def file_name(file: UploadFile):
    return {"filename": file.filename}

# mixed one ==========================

@app.post("/file/fileUplad/file_name")
def file_data(file_name : UploadFile,file_size:bytes=File(),name :str =Form()):
    return {"fileName": file_name.filename,"file_size": len(file_size),"name ": name}

# print("dsj")++++ERROR HANDLING++++++++++++++

items = {"foo": "The Foo Wrestlers","this":"This","thddsjvkj":"djkfs"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        return HTTPException(status_code=404, detail="Item not found hea",headers="df")
    return {"item": items[item_id]}


@app.get("/items/get/fetch")
def read_time(items1:str):
    if items1 not in items:
        return HTTPException(status_code=400,detail="not there")
    return "found"



templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"))

@app.get("/html/get" ,)
def serve_home(request:Request,title:str,header:str):
    # print(type(title))
    # print(type(header))
    return templates.TemplateResponse("index.html",{"request" :request,"title":title,"header":header} )
 