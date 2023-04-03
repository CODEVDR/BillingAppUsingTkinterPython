import base64
import io
import tkinter.filedialog as filedialog

import mysql.connector as sqlctr
from PIL import Image, ImageTk

# Backend

def submit(h, u, p, name, fname, adhrno, addr, mobno, bldgrp, dob, file):
    try:
        con_server = sqlctr.connect(
            host=f"{h}", user=f"{u}", password=f"{p}")
        cs = con_server.cursor()
        cs.execute("create database if not exists user_data;")
        con_database = sqlctr.connect(
            host=f"{h}", user=f"{u}", password=f"{p}", database="user_data")
        cd = con_database.cursor()
        q1 = "create table if not exists data(name varchar(60),fname varchar(60),aadno bigint primary key,addr varchar(90),mobno bigint,bldgrp varchar(10),dob varchar(50),img longblob);"
        args = (f"{name}", f"{fname}", f"{adhrno}", f"{addr}",
                f"{mobno}", f"{bldgrp}", f"{dob}", file)
        q2 = """insert into data values(%s,%s,%s,%s,%s,%s,%s,%s);"""
        cd.execute(q1)
        cd.execute(q2, args)
        con_server.commit()
        con_database.commit()
        val = 1
    except:
        val = 0
    return val



# Upload File


def upload_file(image_area):
    global img  # Image upload and display
    f_types = [('Png files', '*.png'),
               ('Jpg Files', '*.jpg'),("All Files","*.*")]
    filename = filedialog.askopenfilename(
        filetypes=f_types)
    if filename != "":
        filename = filename.replace("\\", "/")
        img = Image.open(filename)
        r_img = img.resize((200, 200))
        img = ImageTk.PhotoImage(r_img)
        image_area['image'] = img
        file = open(filename, 'rb').read()
        file = base64.b64encode(file)
        return file, filename
    else:
        filename = ""
        return 0, filename
