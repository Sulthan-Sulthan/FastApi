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

@app.post("/credit/transfer")
async def credit_transfer(token:str =Depends(oauth_scheme), dest_user_name:str = Body(...), ammount:float = Body(...)):
    # print(token)
    # print(dest_user_name)
    # print(ammount)

    with open("userBalance.json","r") as userBalance_file:
        userBalance_data = json.load(userBalance_file)
        current_userBalance = userBalance_data.get(token)['current_balance']
        # print(f"user balance {current_userBalance}")
        dest_user = userBalance_data.get(dest_user_name)
        if not dest_user:
                raise HTTPException(status_code=400, detail=" Destination user not found")
        dest_user_bal = dest_user["current_balance"]
        if current_userBalance - ammount < 0:
             raise HTTPException(status_code=400, detail=" Ammount is not sufficient")
        userBalance_data[token]["current_balance"] -= ammount
        userBalance_data[dest_user_name]["current_balance"] += ammount
        with open("userBalance.json" , "w") as userBal_write:
             json.dump(userBalance_data , userBal_write)
    return {"Detail " : f"ammount {ammount} has been transferred to {dest_user_name} "
           }



    # return userBalance_data.get(token)["current_balance"]
    
    
