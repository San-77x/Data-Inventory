from fastapi import FastAPI, Body, Request, File, UploadFile, Form
from pydantic import BaseModel #for sending the value from in group
from fastapi.templating import Jinja2Templates #for loading the html 
from fastapi.responses import HTMLResponse #for getting the response from 
# from typing import List

app = FastAPI()



list_of_usernames = list()
templates = Jinja2Templates(directory="HTML") #for loading the html pagfe and tp get input from input path for the html

class NameValues(BaseModel):
    name: str = None
    country: str 
    age:int
    base_salary: float
    

@app.get("/amazon/{user_name}", response_class= HTMLResponse)  

def write_home(request: Request, user_name: str):  #to limit the input types
    return templates.TemplateResponse("amazon.html",{"request":request,"username":user_name})



@app.post("/submitform")
async def handle_form(Product: str = Form(...), Product_File: UploadFile= File(...)):   #async we are saying that 
    print(Product)
    print(Product_File.filename)
    content_product= await Product_File.read()
    print(content_product)

    

        
@app.post("/postData")
def post_data(name_value: NameValues,rider_status: str = Body(...)):
    print(name_value)
    print(name_value)
    
    return{
        "name": name_value.name,
        "rider_status": rider_status
    }