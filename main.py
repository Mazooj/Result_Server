from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.variables import getData, insert_user, write_json, getId
from testingAuthy import *
from config.db import stuinfos, conn, engine
import pandas as pd

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates/')
temp_saved_number = None


@app.get('/')
async def home_page(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request})


@app.get('/adminlogin')
async def adminlogin_page(request: Request):
    return templates.TemplateResponse('adminlogin.html', context={'request': request})


@app.post('/adminlogin')
async def adminlogin_page(request: Request, username: str = Form(...), password: str = Form(...)):
    username = username
    password = password
    if username == 'mazooz' and password == 'mazooz':
        return templates.TemplateResponse('form.html', context={'request': request})
    else:
        return templates.TemplateResponse('redirect.html',
                                          context={'request': request, 'message': 'Wrong Credentials, Try again !'})


@app.post('/submitadminform')
async def post_data(request: Request, fileSelect: UploadFile = File(...)):
    content_file = await fileSelect.read()
    pf = pd.read_excel(content_file)
    pf.to_sql('stuinfos', con=engine)
    getData()
    insert_user()
    write_json()
    return templates.TemplateResponse('redirect.html', context={'request': request, 'message': 'Successfully Done'})


@app.get('/stulogin')
async def stulogin_page(request: Request):
    return templates.TemplateResponse('stulogin.html', context={'request': request})


@app.post('/stulogin')
async def stulogin_page(request: Request, phone: str = Form(...)):
    global temp_saved_number
    temp_saved_number = phone
    authid = getId(phone)
    if authid != None:
        send_otp(authid)
        return templates.TemplateResponse('stulogin.html', context={'request': request})
    else:
        return templates.TemplateResponse('redirect.html', context={'request': request, 'message': 'Invalid Number !'})


@app.get('/table')
async def table_page(request: Request, otp: str):
    global result_data, result_columns, temp_saved_number
    otp = otp
    if len(otp) < 7:
        return templates.TemplateResponse('redirect.html', context={'request': request, 'message': 'Invalid OTP !'})
    result = verify_otp(getId(temp_saved_number), otp)
    if result is True:
        datas = conn.execute(stuinfos.select().where(stuinfos.c.phone == temp_saved_number)).fetchall()
        for dicti in datas:
            result_data = dicti.values()
            result_columns = dicti.keys()
        return templates.TemplateResponse('table.html', context={'request': request, 'headings': result_columns,
                                                                 'datas': result_data})
    else:
        return templates.TemplateResponse('redirect.html', context={'request': request, 'message': 'Invalid OTP !'})
