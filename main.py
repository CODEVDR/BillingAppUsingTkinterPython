import base64
import io
import os
import tkinter.messagebox as msg
from datetime import datetime as dt
from tkinter import *

import mysql.connector as sqlctr
import win32api
from PIL import Image, ImageTk

# For Functions
from assets.module import submit, upload_file

"""
mFrame & mFrame1 are 2 main Frames mFrame For storing data mFrame1 for seeing data 
tmpFrame That Stores Different Buttons With Diff Funcanalities
"""

# Frontend
root = Tk()
root.title("USER INFO | SCA")
root.iconbitmap("assets/icon.ico")
root.minsize(600, 850)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
# bg color control
bcg = "#7FCDD4"
root.config(background="#7FCDD4")
# 892CDC
# bg image
img = Image.open("assets/bg.jpg")
r_img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg = ImageTk.PhotoImage(r_img)
label17 = Label(root, image=bg)
label17.place(x=0, y=0)
# -----------------------CODE STARTS FROM HERE-----------------------


def back():
    root.title("USER INFO | SCA")
    tmpFrame()


mFrame = Frame(root, bg=bcg)
Button(mFrame, text=u"\u25C0 Back", command=back).pack(anchor=W)
Label(mFrame, text="Shyam Computer Academy", font="impact 19 bold",
      relief=SOLID, borderwidth=3).pack(pady=20)

frame_img = Frame(mFrame, bg=bcg)


def upld_file():
    global file
    file = upload_file(image_area1)
    if file[0] == 0:
        msg.showwarning("Warning! | SCA", "No Image Selected")
    else:
        msg.showinfo("Image | SCA", f"{file[1]} selected")


# Setting Image To Button
Label(frame_img, text="IMAGE", relief=SOLID,
      font="Corbel 12 bold underline", fg="black").pack()
img = Image.open("assets/up_img.png")
r_img = img.resize((200, 200))
image = ImageTk.PhotoImage(r_img)
image_area1 = Button(frame_img, image=image, width=200,
                     height=200, relief=GROOVE, command=upld_file)
image_area1.pack()
frame_img.pack()

frame_fields = Frame(mFrame, bg=bcg)
# Variables
name = StringVar()
fname = StringVar()
regNo = IntVar()
adhrno = IntVar()
addr = StringVar()
mobno = IntVar()
dob = StringVar()
# Entries and Labels
Label(frame_fields, text="Name",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=name,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="Father's Name",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=fname,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="Registration Number",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=regNo,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="Aadhaar Number",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=adhrno,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="Address",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=addr,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="Mobile Number",
      relief=SOLID, font="Corbel 10 bold underline", fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=mobno,
      relief=SOLID, font="Corbel 13 bold", width=50).pack()

Label(frame_fields, text="DOB", relief=SOLID, font="Corbel 10 bold underline",
      fg="black").pack(anchor=W)
Entry(frame_fields, textvariable=dob, relief=SOLID,
      font="Corbel 13 bold", width=50).pack()
# Function For Storing Values


def sub():
    try:
        if name.get() == "" or fname.get() == "" or regNo.get() == "" or adhrno.get() == "" or addr.get() == "" or mobno.get() == ""  or dob.get() == "" or file == "":
            print(name.get(),fname.get(),regNo.get(),adhrno.get(),addr.get(),mobno.get(),dob.get(),file)
            msg.showerror("Error | SCA ", "Fields Cant Be Empty")
        else:
            v = msg.askquestion("Submit | SCA",
                                "Do You Want To Submit ?")
            if v == "yes":
                an = submit(hs, us, pw, name.get(), fname.get(),regNo.get(),adhrno.get(
                ), addr.get(), mobno.get(), dob.get(), file[0])
                if an != 0:
                    msg.showinfo("Sucess | SCA ", "Stored Sucessfully")
                else:
                    msg.showerror(
                        "Error | SCA ", "An Error Occured May Be Due To Repetation of registration number.")
    except:
        msg.showerror("Error | SCA", "Please Select an Image.")


Button(frame_fields, text="Submit", relief=SOLID, font="Corbel 12 bold", command=sub, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
frame_fields.pack(pady=30)

# ===================================CODE FOR SEE DATA OF STUDENT===================================================
mFrame1 = Frame(root, bg=bcg)
bk = Button(mFrame1, text=u"\u25C0 Back", command=back)
bk.pack(anchor=W)
# Frame For Getting Required Information To SEarch
# Funtions That Fetchs Data From Server And Responds


def see():
    if name12.get() != "" or regno1.get() != "":
        def showData():
            try:
                cd_Con = sqlctr.connect(
                    host=hs, user=us, password=pw, database="user_data")
                cd = cd_Con.cursor()
                q1 = f"""select * from data where name="{name12.get()}" and regno={regno12.get()};"""
                cd.execute(q1)
                res = cd.fetchall()
                if res == []:
                    return 0, None
                else:
                    return res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6], res[0][7]
            except:
                return 2, None
        v1 = showData()
        if v1[0] == 0:
            msg.showerror("Error | SCA ",
                          "No Such Data is Present in Database")
        elif v1[0] == 2:
            msg.showwarning("Warning | SCA ",
                            "Please Create Table First")
        else:
            try:
                global image3, image_area, bk_to_see

                bk.pack_forget(), gdata_frame.pack_forget()
                name3, fname3,regno3,adhrn3, addr3, mobno3, dob3 = v1[
                    0], v1[1], v1[2], v1[3], v1[4], v1[5], v1[6]

                bsFrame = Frame(mFrame1, bg=bcg)

                def backtoSee():
                    bsFrame.pack_forget()
                    bk.pack(anchor=W)
                    gdata_frame.pack()
                    bk_to_see.pack_forget()

                bk_to_see = Button(
                    mFrame1, text=u"\u25C0 Back", command=backtoSee)
                bk_to_see.pack(anchor=W)
                Label(bsFrame, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
                      font="impact 25 bold underline", fg="black").pack(pady=50)
                # For Showing Image
                binary_data = base64.b64decode(v1[7])
                img = Image.open((io.BytesIO(binary_data)))
                r_img = img.resize((200, 200))
                image3 = ImageTk.PhotoImage(r_img)
                image_area = Button(bsFrame, image=image3, width=200,
                                    height=200, relief=SOLID, borderwidth=3)
                image_area.pack(pady=50)
                # ``````````````ENDS``````````````
                Label(bsFrame, text=f"Name : {name3}", relief=SOLID,
                      font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"Father's Name : {fname3}", relief=SOLID,
                      font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"Registration Number : {regno3}",
                      relief=SOLID, font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"Aadhaar Number : {adhrn3}",
                      relief=SOLID, font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"Address : {addr3}", relief=SOLID,
                      font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"Mobile Number : {mobno3}", relief=SOLID,
                      font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)
                Label(bsFrame, text=f"DOB : {dob3}", relief=SOLID,
                      font="Corbel 15 bold underline", width=50, fg="black").pack(pady=5)

                bsFrame.pack()
            except:
                pass
    else:
        msg.showerror("Error | SCA ", "Fields Can't Be Empty")


gdata_frame = Frame(mFrame1, bg=bcg)
name12 = StringVar()
regno12 = StringVar()
Label(gdata_frame, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=100)
Label(gdata_frame, text="Enter Name", relief=SOLID, font="Corbel 15 bold underline",
      fg="black").pack(anchor=W)
Entry(gdata_frame, textvariable=name12, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
gdata_frame.pack()
Label(gdata_frame, text="Enter Registration Number", relief=SOLID, font="Corbel 15 bold underline",
      fg="black").pack(anchor=W)
Entry(gdata_frame, textvariable=regno12, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
Button(gdata_frame, text="Submit", relief=SOLID, font="Corbel 12 bold", command=see, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
gdata_frame.pack()
# ========================================================================================
# End of Aboove Code


# ----------------------------------For Payment Window-----------------------------------
mFrame2 = Frame(root, bg=bcg)
global addFeeStruc, storePayment, seePayment
bkmFrame2 = Button(mFrame2, text=u"\u25C0 Back", command=back)
bkmFrame2.pack(anchor=W)  # For Main Exit


def localBack():
    try:
        addFeeStruc.pack_forget(), storePayment.pack_forget(
        ), seePayment.pack_forget(), seePaymentH.pack_forget()
    except:
        pass
    bkmFrame2.pack(anchor=W), frmOption.pack()


# Options Code addFeeStruc #DONE
addFeeStruc = Frame(mFrame2, bg=bcg)
# For Temp connection


Button(addFeeStruc, text=u"\u25C0 Back", command=localBack).pack(anchor=W)
Label(addFeeStruc, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=100)
# For Adding Fee Stucture
addFeestruc = Frame(addFeeStruc, bg=bcg)
# Function That Stores Fee


def storeFee():
    cd = sqlctr.connect(host=hs, user=us, password=pw)
    cur = cd.cursor()
    cur.execute("use user_data;")
    q1 = "create table if not exists feeStruc(cName varchar(30) primary key,cFee varchar(20));"
    cur.execute(q1)
    if cName.get() == "" or cFee.get() == "":
        msg.showerror("Error | SCA", "Fields Can't Be Empty")
    else:
        try:
            q2 = f"""insert into feeStruc values("{cName.get()}","{cFee.get()}");"""
            cur.execute(q2)
            msg.showinfo("Sucess | SCA", "Data Stored Sucessfully")
        except:
            msg.showerror("Error | SCA", "Data Already Exists")
    cd.commit()


# Variables
cName = StringVar()
cFee = StringVar()
Label(addFeestruc, text="Course Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(addFeestruc, textvariable=cName, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(addFeestruc, text="Course Fee", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(addFeestruc, textvariable=cFee, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Button(addFeestruc, text="Submit", relief=SOLID, font="Corbel 12 bold", command=storeFee, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)

addFeestruc.pack()
# --------------------------------------------
# End Of Add Fee Struc code


# -------------------A Frame To Store Fee Payment-------------------------
# Options Code storePayment #DONE
storePayment = Frame(mFrame2, bg=bcg)
Button(storePayment, text=u"\u25C0 Back", command=localBack).pack(anchor=W)
Label(storePayment, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=100)


def storeFeeServ():
    cd = sqlctr.connect(host=hs, user=us, password=pw)
    cur = cd.cursor()
    cur.execute("use user_data;")
    q1 = "create table if not exists studFee(regNo varchar(30),cName varchar(40),amtFee varchar(20),date varchar(90));"
    cur.execute(q1)
    if regno.get() == "" or amtFee.get() == "":
        msg.showerror("Error | SCA", "Fields Can't Be Empty")
        cd.commit()
    else:
        try:
            q2 = f"""select * from data where regno={regno.get()};"""
            cur.execute(q2)
        except:
            msg.showerror("Error", "Please Create table First")
        res = cur.fetchall()
        if res == []:
            msg.showerror("Error | SCA",
                          "No Such Registration Number Found In Database")
            cd.commit()
        else:
            q3 = f"""select * from feeStruc where cName="{csName.get()}";"""
            cur.execute(q3)
            res1 = cur.fetchall()
            if res1 == []:
                msg.showerror("Error | SCA", "Fee Struc Not Defined")
                cd.commit()
            else:
                s = str(dt.now()).split(" ")
                q4 = f"""insert into studFee values("{regno.get()}","{csName.get()}","{amtFee.get()}","{s[0]}");"""
                cur.execute(q4)

                # For Remaining Fee
                ttlFee = int(res1[0][1])
                cur.execute(
                    f"select * from studfee where regNo='{regno.get()}';")
                v = cur.fetchall()
                fPaid = 0
                for i in v:
                    fPaid += int(i[2])
                remFee = ttlFee-fPaid
                if remFee <= 0:
                    amtrem["text"] = "Total Fee Paid"
                    msg.showinfo("Sucess | SCA", "Total Fee Paid")
                else:
                    amtrem["text"] = f"Remaining Fee {remFee}"
                    msg.showinfo("Sucess | SCA",
                                 "Data Stored Sucessfully")

                amtFee.set("")
                cd.commit()


# Variables
regno = StringVar()
csName = StringVar()
amtFee = StringVar()
Label(storePayment, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(storePayment, textvariable=regno, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(storePayment, text="Course Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(storePayment, textvariable=csName, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(storePayment, text="Amount Paid", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(storePayment, textvariable=amtFee, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

amtrem = Label(storePayment, text="", relief=SOLID, borderwidth=3,
               font="Corbel 15 bold underline", fg="black")
amtrem.pack(anchor=W)

Button(storePayment, text="Submit", relief=SOLID, font="Corbel 12 bold", command=storeFeeServ, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
# --------------------------------------------
# End Of Store Payment Code


# ----------------------------A Frame To See Print Current Payment History--------------------------------
# Options Code seePayment (Includes Printing Of Data also)
seePayment = Frame(mFrame2, bg=bcg)
bksp = Button(seePayment, text=u"\u25C0 Back", command=localBack)
bksp.pack(anchor=W)
head = Label(seePayment, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
             font="impact 25 bold underline", fg="black")
head.pack(pady=50)


def seeFeeServ():
    # Frame For See Payment History
    pmWndw = Frame(seePayment, bg=bcg)
    # Function For Back

    def back2fmTemp():
        pmWndw.pack_forget(), btnbk.pack_forget()
        bksp.pack(anchor=W), head.pack(pady=50), fmTemp.pack()
    global image_area1, image4
    cd_con = sqlctr.connect(
        host=hs, user=us, password=pw, database="user_data")
    cd = cd_con.cursor()
    q1 = f"select * from data where name='{nm.get()}' && regno={regno1.get()};"
    cd.execute(q1)
    res10 = cd.fetchall()

    if res10 == []:
        msg.showerror("Error | SCA", "No Data Found")
    else:
        try:
            btnbk = Button(pmWndw, text=u"\u25C0 Back", command=back2fmTemp)
            btnbk.pack(anchor=W)
            Label(pmWndw, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
                  font="impact 25 bold underline", fg="black").pack(pady=50)
            bksp.pack_forget(), fmTemp.pack_forget(), head.pack_forget()
            name4, fname4, adhrn4, addr4, mobno4, bldgrp4, dob4 = res10[0][0], res10[
                0][1], res10[0][2], res10[0][3], res10[0][4], res10[0][5], res10[0][6]
            Label(pmWndw, text=f"Image", relief=SOLID,
                  font="Corbel 15 bold underline", fg="black").pack()
            # For Showing Image
            binary_data = base64.b64decode(res10[0][7])
            img = Image.open((io.BytesIO(binary_data)))
            r_img = img.resize((200, 200))
            image4 = ImageTk.PhotoImage(r_img)
            image_area1 = Button(pmWndw, image=image4, width=200,
                                 height=200, relief=SOLID, borderwidth=3)
            image_area1.pack()

            txtArea = Text(pmWndw, height=12, width=80,
                           bg="light cyan", relief=SOLID, font="Corbel 14 bold")
            # For insertion
            # For cource
            cd.execute(f"select * from studfee where regno='{res10[0][2]}';")
            result = cd.fetchall()
            s1 = f"""
\t\t\tSHAYAM COMPUTER ACADEMY
\t\tNAME           : {res10[0][0]}
\t\tCOURSE         : {result[0][1]}
\t\tREGISTRATION NUMBER : {adhrn4}

\t\tBILL DATE :   {result[0][3]}          AMOUNT : {result[-1][2]}     \t

\t\t**THIS IS AN COMPUTER GENERATED BILL
"""
# For Print
            v = u"\u2702"
            s2 = f"""
            SHAYAM COMPUTER ACADEMY
NAME           : {res10[0][0]}
COURSE         : {result[0][1]}
REGISTRATION NUMBER : {adhrn4}

BILL DATE : {result[0][3]}     AMOUNT : {result[-1][2]}

**THIS IS AN COMPUTER GENERATED BILL
{v}---------------------------------------
"""
            txtArea.insert(INSERT, s1)
            txtArea.pack(pady=20)
            # Function to print

            def printf():
                os.chdir("assets")
                with open("temp.txt", "w", encoding="utf-8") as f:
                    f.write(s2)
                    f.close()
                file_to_print = "temp.txt"
                if file_to_print:
                    win32api.ShellExecute(
                        0, "print", file_to_print, None, ".", 0)
                os.chdir("..")
            Button(pmWndw, text="🖨️Print", command=printf, relief=SOLID, font="Corbel 12 bold", fg="black",
                   activebackground="grey", activeforeground="black", width=40).pack(pady=10)
        except:
            msg.showerror("Error | SCA", "Please Create Table First")
    pmWndw.pack()


fmTemp = Frame(seePayment, bg=bcg)
# Variables
nm = StringVar()
regno1 = StringVar()
Label(fmTemp, text="Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp, textvariable=nm, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(fmTemp, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp, textvariable=regno1, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Button(fmTemp, text="Submit", relief=SOLID, font="Corbel 12 bold", command=seeFeeServ, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
fmTemp.pack(pady=50)
# --------------------------------------------
# END of Above Part i.e. printing data


# ------------------------------A Frame To See Payment History---------------------------------
seePaymentH = Frame(mFrame2, bg=bcg)
bksp1 = Button(seePaymentH, text=u"\u25C0 Back", command=localBack)
bksp1.pack(anchor=W)
head1 = Label(seePaymentH, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
              font="impact 25 bold underline", fg="black")
head1.pack(pady=50)


def seeFeeServ1():
    # Frame For See Payment History
    pmWndw = Frame(seePaymentH, bg=bcg)
    # Function For Back

    def back2fmTemp():
        pmWndw.pack_forget(), btnbk.pack_forget()
        bksp1.pack(anchor=W), head1.pack(pady=50), fmTemp1.pack()
    global image_area1, image4
    cd_con = sqlctr.connect(
        host=hs, user=us, password=pw, database="user_data")
    cd = cd_con.cursor()
    q1 = f"select * from data where name='{nm15.get()}' && regno={regno115.get()};"
    cd.execute(q1)
    res101 = cd.fetchall()
    if res101 == []:
        msg.showerror("Error | SCA", "No Data Found")
    else:
        try:
            btnbk = Button(pmWndw, text=u"\u25C0 Back", command=back2fmTemp)
            btnbk.pack(anchor=W)
            Label(pmWndw, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
                  font="impact 20 bold underline", fg="black").pack(pady=50)
            bksp1.pack_forget(), fmTemp1.pack_forget(), head1.pack_forget()
            name4, fname4, adhrn4, addr4, mobno4, bldgrp4, dob4 = res101[0][0], res101[
                0][1], res101[0][2], res101[0][3], res101[0][4], res101[0][5], res101[0][6]
            Label(pmWndw, text=f"Image", relief=SOLID,
                  font="Corbel 15 bold underline", fg="black").pack()
            # For Showing Image
            binary_data = base64.b64decode(res101[0][7])
            img = Image.open((io.BytesIO(binary_data)))
            r_img = img.resize((200, 200))
            image4 = ImageTk.PhotoImage(r_img)
            image_area1 = Button(pmWndw, image=image4, width=200,
                                 height=200, relief=SOLID, borderwidth=3)
            image_area1.pack()

            txtArea = Text(pmWndw, height=15, width=80,
                           bg="light cyan", relief=SOLID, font="Corbel 20 bold")
            # For insertion
            # For cource
            cd.execute(f"select * from studfee where regno='{res101[0][2]}';")
            result = cd.fetchall()
            s1, total = "", 0
            s1 += "Reg.No. Course AmtPaid Date\n"
            for i in result:
                total += int(i[2])
                s1 += f"{i[0]} , {i[1]} , {i[2]} , {i[3]}\n"
            s1 += f"\nTotal Fee Paid Till Now : {total}"
            # Insertion End
            txtArea.insert(INSERT, s1)
            txtArea.pack(pady=20)
        except:
            msg.showerror("Error | SCA", "Please Create Table First")
    pmWndw.pack()


# --------------------------------------------------------------------------------------------
fmTemp1 = Frame(seePaymentH, bg=bcg)
# Variables
nm15 = StringVar()
regno115 = StringVar()
Label(fmTemp1, text="Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp1, textvariable=nm15, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(fmTemp1, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp1, textvariable=regno115, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Button(fmTemp1, text="Submit", relief=SOLID, font="Corbel 12 bold", command=seeFeeServ1, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
fmTemp1.pack(pady=50)


# Form Here Options of Payment window Starts
# ---------------------------------------------------------------------------------------------
# options Fuction


def addfeeStruc():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    addFeeStruc.pack()


def storepayment():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    storePayment.pack()


def seepayment():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    seePayment.pack()


def seepaymentHis():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    seePaymentH.pack()


frmOption = Frame(mFrame2, bg=bcg)
Label(frmOption, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=100)
Button(frmOption, text="Add Course Structure", command=addfeeStruc, relief=SOLID, font="Corbel 12 bold", fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
Button(frmOption, text="Store Payment", command=storepayment, relief=SOLID, font="Corbel 12 bold", fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
Button(frmOption, text="See Payment History", command=seepaymentHis, relief=SOLID, font="Corbel 12 bold", fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
Button(frmOption, text="Print Current Payment Details", command=seepayment, relief=SOLID, font="Corbel 12 bold", fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
frmOption.pack()
# =========================================================================================
# End Of Payment Window
# -----------------------------------A Frame For Deletion Of Student Data-----------------------------------
mFrame3 = Frame(root, bg=bcg)
fmTemp_ = Frame(mFrame3, bg=bcg)


def lclBack():
    root.title("STORE DATA | SCA")
    tmpFrame()


# For Back
back_ = Button(fmTemp_, text=u"\u25C0 Back", command=lclBack)
back_.pack(anchor=W)
# Heading
Label(fmTemp_, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=70)
# Variables
name_ = StringVar()
regno_ = StringVar()

Label(fmTemp_, text="Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp_, textvariable=name_, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(fmTemp_, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(fmTemp_, textvariable=regno_, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
var_ = IntVar()
Checkbutton(fmTemp_, text="Also Delete Fee Data", font="Corbel 14 bold",
            fg="black", variable=var_, bg=bcg).pack(anchor=W)
# Deletes Server Password


def deleteServ():
    if name_.get != "" and regno_.get() != "":
        cd_con_ = sqlctr.connect(
            host=hs, user=us, password=pw, database="user_data")
        cd_ = cd_con_.cursor()
        q1_ = f"select * from data where name='{name_.get()}' && regno={regno_.get()};"
        cd_.execute(q1_)
        res = cd_.fetchall()
        if res != []:
            if var_.get() == 1:
                ask = msg.askquestion(
                    "Delete | SCA", "Sure To Delete Data Including Fee Data Also")
            else:
                ask = msg.askquestion("Delete | SCA", "Sure To Delete Data")
            if ask == "yes":
                cd_.execute(
                    f"delete from data where name='{name_.get()}' && regno={regno_.get()};")
                if var_.get() == 1:
                    try:
                        cd_.execute(
                            f"delete from studfee where regno={regno_.get()};")
                    except:
                        msg.showerror("Error | SCA", "No Fee Data in Database")
                    var_.set(0)
                msg.showinfo("Deleted | SCA", "Data Deleted")
                cd_con_.commit()
            else:
                msg.showinfo("Not Deleted | SCA", "Data Not Deleted")
        else:
            msg.showerror("Error | SCA", "Error No Data Found")
    else:
        msg.showerror("Error | SCA", "Fields Can't Be Empty")


Button(fmTemp_, text="Submit", relief=SOLID, font="Corbel 12 bold", command=deleteServ, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
fmTemp_.pack(pady=50)
# ----------------------------------------------------------------------------------------------------------
# End of Deletion Data


# NOTICE
"""
CONTROL OVER ALL FRAMES
"""


def tmpFrame():
    # Temporary Frame
    tFrame = Frame(root, bg=bcg)
    try:
        mFrame.pack_forget(), mFrame1.pack_forget(
        ), mFrame2.pack_forget(), mFrame3.pack_forget()
    except:
        pass

    Label(tFrame, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
          font="impact 25 bold underline", fg="black").pack(pady=100)
    # Functions

    def storeData():
        root.title("STORE DATA | SCA")
        tFrame.pack_forget()
        mFrame.pack()

    def seeData():
        root.title("SEE DATA | SCA")
        tFrame.pack_forget()
        mFrame1.pack()

    def deleteData():
        root.title("DELETE DATA | SCA")
        tFrame.pack_forget()
        mFrame3.pack()

    def paymentWindow():
        root.title("PAYMENT WINDWOW | SCA")
        tFrame.pack_forget()
        mFrame2.pack()
        # msg.showinfo("Under Development | SCA","The Window Was Under Development....")

    def EXIT():
        try:
            os.remove("assets/temp.txt")
        except:
            pass
        root.destroy()
    # Adding Diffrent Buttons For Diffeent Work
    Button(tFrame, text="Store Data", relief=SOLID, font="Corbel 12 bold", fg="black",
           activebackground="grey", activeforeground="black", command=storeData, width=40).pack(pady=10)
    Button(tFrame, text="See Data", relief=SOLID, font="Corbel 12 bold", fg="black",
           activebackground="grey", activeforeground="black", command=seeData, width=40).pack(pady=10)
    Button(tFrame, text="Delete Data", relief=SOLID, font="Corbel 12 bold", fg="black",
           activebackground="grey", activeforeground="black", command=deleteData, width=40).pack(pady=10)
    Button(tFrame, text="Payment Window", relief=SOLID, font="Corbel 12 bold", fg="black",
           activebackground="grey", activeforeground="black", command=paymentWindow, width=40).pack(pady=10)
    Button(tFrame, text="EXIT", relief=SOLID, font="Corbel 12 bold", fg="black",
           activebackground="grey", activeforeground="black", command=EXIT, width=40).pack(pady=10)
    tFrame.pack()
    # ========================================================================

# Starts From Here Login Window


def pw_get():
    global hs, us, pw, tFrame

    try:
        cs = sqlctr.connect(
            host=f"{host.get()}", user=f"{user.get()}", password=f"{password.get()}")
        cs_cur = cs.cursor()
        cs_cur.execute("create database if not exists user_data;")
        cs_cur.execute("use user_data;")
        hs, us, pw = host.get(), user.get(), password.get()
        msg.showinfo("Sucess | SCA", "Logged In Sucessfully")
        frame.pack_forget()
        tmpFrame()
    except ModuleNotFoundError:
        msg.showerror("Error | SCA",
                      "Might Sql is not installed or You Are Using The\nOlder version of My Sql Please Install My Sql")
    except:
        msg.showerror("Error | SCA", "Incorrect Credentials")


frame = Frame(root, bg=bcg)
Label(frame, text="Shyam Computer Academy", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="black").pack(pady=100)
host = StringVar()
user = StringVar()
password = StringVar()
# Labels and Entries
Label(frame, text="Enter Host", relief=SOLID, font="Corbel 15 bold underline",
      fg="black").pack(anchor=W)
Entry(frame, textvariable=host, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
Label(frame, text="Enter User", relief=SOLID, font="Corbel 15 bold underline",
      fg="black").pack(anchor=W)
Entry(frame, textvariable=user, relief=SOLID,
      font="Corbel 20 bold", show="*", width=50).pack()
Label(frame, text="Enter Server Password",
      relief=SOLID, font="Corbel 15 bold underline", fg="black").pack(anchor=W)
Entry(frame, textvariable=password,
      relief=SOLID, font="Corbel 20 bold", show="*", width=50).pack()
Button(frame, text="Submit", relief=SOLID, font="Corbel 12 bold", command=pw_get, fg="black",
       activebackground="grey", activeforeground="black", width=40).pack(pady=10)
frame.pack()


root.mainloop()
# Created by SCA
# Copyrighted content
