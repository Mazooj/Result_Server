import json
from config.db import engine
import pandas as pd
from testingAuthy import add_user

names = []
phone = []
email = []
authy_id = []
dic = {}
dic2 = {}


def write_json():
    global dic
    with open('data.json', 'r+') as file:
        json.dump(dic, file)
    with open('data2.json', 'r+') as file2:
        json.dump(dic2, file2)


def getId(number):
    file = open('data2.json', 'r')
    data = json.load(file)
    try:
        return data[number]['auth_id']
    except Exception:
        return None


def getData():
    global names, phone, email
    query = 'SELECT stu_name,phone,email FROM stuinfos'
    df = pd.read_sql_query(query, engine)
    ndf = df.convert_dtypes()
    none_val = pd.NA
    for i in range(20):
        if ndf.phone[i] is not none_val and ndf.email[i] is not none_val:
            names.append(ndf.stu_name[i])
            phone.append(str(ndf.phone[i]))
            email.append(ndf.email[i])
    return names, phone, email


def insert_user():
    global names, phone, email, dic, authy_id, dic2
    for i in range(len(names)):
        authid = add_user(email[i], phone[i])
        authy_id.append(authid)
        dic.update({names[i]: {'phone': phone[i], 'authy_id': authy_id[i]}})
        dic2.update({phone[i]: {'name': names[i], 'authy_id': authy_id[i]}})
    return dic, dic2
