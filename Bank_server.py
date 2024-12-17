from fastapi import FastAPI ,Body,Request
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json


app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/home")
def Home_page():
    return "Home"

@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm = Depends()):
    with open("user_db.json","r") as json_file:
        json_data = json.load(json_file)
        if json_data:
            password = json_data.get(form_data.username)
            if not password:
                print("wrong user name or password ")
                raise HTTPException(status_code=400, detail="Inactive user")


    # print(f"THIS IS FORM DATA {form_data}")
    return {"access_token":form_data.username , "token_type":"bearer"}


@app.get("/spend/history")
async def spend(token:str=Depends(oauth_scheme)):
    with open("spend_history.json","r") as spend_history_file:
        spend_history_data = json.load(spend_history_file)
        if not spend_history_data[token]:
                raise HTTPException(status_code=400, detail="user not found")
    return {
        "username":token,
        "spend_hist": spend_history_data[token]
    }
    # print(token)



@app.get("/credit/history")
async def credit(token:str=Depends(oauth_scheme)):
    with open("credit.json","r") as credit_history_file:
        credit_history_data = json.load(credit_history_file)
        if not credit_history_data[token]:
                raise HTTPException(status_code=400, detail="user not found")
    return {
        "username1":token,
        "credit_hist": credit_history_data[token]
    }
