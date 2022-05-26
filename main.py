from typing import Optional
from fastapi import FastAPI, Request
from Gmail.Mail import *

# khoi tao app 
app = FastAPI()

# tao hai duong url 
# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# tra ve item game 
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"so_item": item_id}

# tra ve gia tri so 
@app.get("/number/{num}")
def get_number(num: int ):
    return "So ma ban vua nhap vao:" + str(num)

# viet API ng dung se nhap vao chu so de kiem tra laf chan hay le 
@app.get("/check/{so}")
def kiem_tra_chan_le(so: int):
    if so % 2 == 0: return f"So {so} la so chan"
    return f"So {so} la so le!"

@app.get("/saleof100")
def getIPFromClient(request: Request):
    client_ip = request.client.host
    return {"Client_ip": client_ip}

@app.post("/send_email")
def send_email_to_everyone(content: str, receiver: str, subject: str):
    return send_email(content, receiver, subject)  

    