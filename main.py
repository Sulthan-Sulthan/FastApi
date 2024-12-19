from typing import Annotated, Union
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from fastapi import Depends, FastAPI, File, Form, HTTPException, Query, Response,UploadFile,Request,Cookie
from enum import Enum
from pydantic import BaseModel
from new import Sql_operation 


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


class Values_Inserting(BaseModel):
    id: int
    name:str
    salary:int
    dept_name:str



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



# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"))

# @app.get("/html/get" ,)
# def serve_home(request:Request,title:str,header:str):
#     # print(type(title))
#     # print(type(header))
#     return templates.TemplateResponse("index.html",{"request" :request,"title":title,"header":header} )
 

# @app.get("/submit-form", response_class=HTMLResponse)
# async def show_form(request:Request ):
#     return templates.TemplateResponse("form.html",{"request" :request} )


@app.post("/submit-form/form")
async def submit_form(request:Request,name:str=Form(),email:str=Form()):
    return {"name":name,"email":email}



# +++++++++++++++cookie+=============


@app.get("/set/cookies/")
async def set_cookie(response : Response):
    response.set_cookie(key="faris",value="raasoft")
    return {"message": "cookies set successful"}


# ===========get cookies===========

@app.get("/get/cookies/")
async def get_cookie(request:Request):
    value = request.cookies.get("faris")
    return {"cookie":value}

def get_dependiecies_db():
    return "fake one "

def get_fun():
    return "real one"


@app.get("/dependicies")
async def deapendecies(db:str=Depends(get_dependiecies_db),current_user:str=Depends(get_fun)):
    return {"db_connection":db,"current_user":current_user}



db = Sql_operation()
@app.on_event("startup")
async def startup_event():
    db.creating_table()







@app.post("/items/", status_code=201)
async def create_data(item: Values_Inserting):
    try:
        db.inserting_values(item.id,item.name,item.salary,item.dept_name)
        return { "message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    





@app.put("/items2152")
async def update(name:str):
    try:
        db.update(name)
        return {"message": "Item updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/items/delete/{item_id}")
async def delete_item(item_id: int):
    try:
        db.delete(item_id)
        return {"message": f"Item {item_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


