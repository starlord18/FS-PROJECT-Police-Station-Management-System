import tkinter
from tkinter import *
import tkinter as tk

f = open("policerec.txt", "r")


def insert_pol():
    global id
    top1 = Toplevel()
    top1.title("INSERT POLICE RECORD")
    top1.geometry("500x400")
    top1.config(background= "PaleGreen1")

    pol_name_label = Label(top1, text= "enter name of the police",font="fixedsys")
    pol_name_entry= Entry(top1)
    pol_name_label.grid(row=0)
    pol_name_entry.grid(row= 0, column = 1)

    pol_addr_label = Label(top1, text= "enter police address",font="fixedsys")
    pol_addr_entry= Entry(top1)
    pol_addr_label.grid(row=1)
    pol_addr_entry.grid(row= 1, column = 1)


    pol_contact_label = Label(top1, text= "enter contact no.",font="fixedsys")
    pol_contact_entry= Entry(top1)
    pol_contact_label.grid(row=2)
    pol_contact_entry.grid(row= 2, column = 1)


    pol_cur_label = Label(top1, text= "enter current station",font="fixedsys")
    pol_cur_entry= Entry(top1)
    pol_cur_label.grid(row=3)
    pol_cur_entry.grid(row= 3, column = 1)

    gend = IntVar()
    male = Radiobutton(top1, text = "Male", variable = gend, value =1)
    female = Radiobutton(top1 , text = "Female" , variable = gend , value = 2)
    male.grid(row = 4, column = 0)
    female.grid(row= 4 , column = 1)
    id = 0
    for line in f:
        id+=1
    msg= Text(top1 , width = 500, height = 15)
    msg.grid(row = 5, column= 2)
    n_id = str(id)
    msg_with_id = "last record has id " + n_id
    msg.insert(tk.END,msg_with_id )

    def polsub():
        f = open("policerec.txt", "r")
        id= 0
        for line in f:
            id+=1
        id+=1
        new_id = str(id)
        name = pol_name_entry.get()
        addr = pol_addr_entry.get()
        cont = pol_contact_entry.get()
        cur = pol_cur_entry.get()
        gender= str(gend.get())
        con=""
        flag =0
        f.close();
        f = open("policerec.txt","r")
        for line in f:
            if((line == "*"+"\n") or(line== "\n")) :
                continue
            elif(line!="*"+"\n"):
                field = line.split("|")
                print(field)
                con = field[3]
                if(cont == con):
                    flag = 1
        f.close()
        if(flag == 1):
            msg.delete(0.0,END)
            msg.insert(tk.END,"Duplicate record!")
        else:
            f= open("policerec.txt","a")
            f.write(new_id + "|" + name+"|"+addr+"|"+cont+"|"+cur+"|"+gender+"$"+"\n")
            f.close()
            msg.delete(0.0,END)
            new_msg = "This police has ID "
            new_msg_id = new_msg+new_id
            msg.insert(tk.END,new_msg_id)
    pol_sub_button = Button(top1, text = "submit" ,bg= "brown",command = polsub,font="fixedsys")
    pol_sub_button.grid(row= 6, column= 0)

    pol_home_button = Button(top1, text = "HOME",bg= "orange", command= top1.destroy,font="fixedsys")
    pol_home_button.grid(row= 6 , column = 1)

def insert_crim():
    top2 = Toplevel()
    top2.title("INSERT CRIMINAL RECORD")
    top2.config(background = "DarkGoldenRod1")


    crim_name_label = Label(top2, text= "enter name of the criminal",font="fixedsys")
    crim_name_entry= Entry(top2)
    crim_name_label.grid(row=0)
    crim_name_entry.grid(row= 0, column = 1)

    crim_addr_label = Label(top2, text= " enter criminal's address",font="fixedsys")
    crim_addr_entry= Entry(top2)
    crim_addr_label.grid(row=1)
    crim_addr_entry.grid(row= 1, column = 1)


    crim_contact_label = Label(top2, text= "enter criminal contact no",font="fixedsys")
    crim_contact_entry= Entry(top2)
    crim_contact_label.grid(row=2)
    crim_contact_entry.grid(row= 2, column = 1)

    status =IntVar()
    status1 = Radiobutton(top2, text = "Captive", variable = status , value = 1)
    status2 = Radiobutton(top2, text = "Released", variable = status, value = 0 )
    status1.grid(row = 3, column = 1)
    status2.grid(row = 3, column = 2)
    crim_cur_label = Label(top2, text= "enter current jail",font="fixedsys")
    crim_cur_entry= Entry(top2)
    crim_cur_label.grid(row=4)
    crim_cur_entry.grid(row= 4, column = 1)

    gend = IntVar()
    male = Radiobutton(top2, text = "Male", variable = gend, value =1)
    female = Radiobutton(top2 , text = "Female" , variable = gend , value = 2)
    male.grid(row = 5, column = 1)
    female.grid(row= 5 , column = 2)
    f = open("crimrec.txt","r")
    id = 0
    for line in f:
        id+=1
    msg= Text(top2 , width = 20, height = 20)
    msg.grid(row = 6, column= 2,sticky = S)
    n_id = str(id)
    msg_with_id = "last criminal has id " + n_id
    msg.insert(tk.END,msg_with_id )
    def crimsub():
        global cur
        name = crim_name_entry.get()
        addr = crim_addr_entry.get()
        cont = crim_contact_entry.get()
        status1= str(status.get())
        if(status1 == "1"):
            cur = crim_cur_entry.get()
        else:
            cur = "released"
        gender= str(gend.get())

        f = open("crimrec.txt", "r")
        id= 0
        con=""
        for line in f:
            id+=1
        id+=1
        flag=0
        f.close()
        f = open("crimrec.txt","r")
        for line in f:
            if((line == "*"+"\n") or (line=="\n")):
                continue
            elif( line!="*"+"\n"):
                field = line.split("|")
                print(field)
                con = field[3]
                if(cont == con):
                    flag = 1
        f.close()
        if(flag==1):
            msg.delete(0.0,END)
            msg.insert(tk.END,"Duplicate criminal record!")
        elif(flag!=1):
            msg.delete(0.0,END)
            new_msg = "This criminal has ID "
            new_id = str(id)
            new_msg_id = new_msg+new_id
            msg.insert(tk.END,new_msg_id)
            f = open("crimrec.txt","a")
            f.write((new_id + "|" + name+"|"+addr+"|"+cont+"|" +cur+"|"+gender+"$")+"\n")
            f.close()


    crim_sub_button = Button(top2, text = "submit", command = crimsub,font="fixedsys")
    crim_sub_button.grid(row= 7, column= 0)
    crim_home = Button(top2, text= "HOME", command= top2.destroy, bg = "brown",font="fixedsys" )
    crim_home.grid(row = 7, column =1 )


def search_pol():
    top3 = Toplevel()
    top3.title("SEARCH FOR POLICE RECORDS")
    top3.config(background = "dark slate blue")
    pol_id_label  = Label(top3, text = "enter the id of the police(optional)",font="fixedsys")
    pol_id_entry = Entry(top3)
    pol_id_label.grid(row = 0)
    pol_id_entry.grid(row = 0, column = 1)

    pol_name_label = Label(top3, text = "enter police name",font="fixedsys")
    pol_name_entry = Entry(top3)
    pol_name_label.grid(row = 1)
    pol_name_entry.grid(row = 1, column = 1)


    msg = Text(top3, width = 40, height = 10)
    msg.grid(row = 5, column =0,sticky = W)
    first_msg = "SEARCH RESULT APPEAR HERE"
    msg.insert(tk.END, first_msg)

    def pol_search():
        name=""
        id_1=""
        last=0
        fields = list()
        compl_id = ""
        compl_name=""
        compl_add=""
        compl_cont=""
        compl_cur=""
        compl_gen=""
        compll_msg=""
        gend=""
        addr=""
        cont=""
        cur=""
        id2=0
        id = pol_id_entry.get()
        name1 = pol_name_entry.get()
        flag=0
        f = open("policerec.txt","r")
        if(id):
            id1= int(id)
            for line in f:
                if(line == "*"+"\n"):
                    continue
                elif(line!="*"+"\n"):
                    fields = line.split("|")
                    bin_list = list()
                    dummy = fields[0]
                    ID = int(dummy)
                    bin_list.append(ID)
                    print((type(bin_list[0])))
                high = len(bin_list)-1
                print(high)
                low = 0
                while(high>=low):
                    mid = (low+high)//2
                    if (bin_list[mid]==id1):
                        flag=1
                        break
                    elif(bin_list[mid]<id1):
                        low= mid+1
                    elif(bin_list[mid]>id1):
                        high = mid-1
            f.close()
            f=open("policerec.txt","r")
            l =list()
            if(flag==1):
                for line in f:
                    if(line=="*"+"\n"):
                        continue
                    elif(line!="*"+"\n"):
                        l = line.split("|")
                        print(l)
                        ID1 = l[0]
                        ID2 = int(ID1)
                        if(ID1==id):
                            msg.delete(0.0,END)
                            compl_id = "id :"+l[0]+"\t"
                            compl_name = "name: "+l[1]+"\t"
                            compl_add = "address: "+l[2]+"\t"
                            compl_cont = "contact: "+l[3]+"\t"
                            compl_cur = "Current station: "+l[4]+"\t"
                            compl_gen = "Gender: "+ gend+"\t"
                            compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                            msg.insert(tk.END, compll_msg)
            elif(flag==0):
                 msg.delete(0.0,END)
                 msg.insert(tk.END,"NO RECORD FOUND!")


        elif name1:
            for line in f:
                if (name1+"|") not in line:
                    continue
                elif(name1+"|") in line:
                    fields = line.split("|" or "$")
                    id_1 = fields[0]
                    id2 = int(id_1)
                    name = fields[1]
                    addr = fields[2]
                    cont = fields[3]
                    cur = fields[4]
                    gen = fields[5]
                    if (gen == "1$"):
                        gend = "Male"
                    elif(gen=="2$"):
                        gend = "Female"
                    msg.insert(tk.END,"\n")
                    compl_id = "id :"+id_1+"\t"
                    compl_name = "name: "+name+"\t"
                    compl_add = "address: "+addr+"\t"
                    compl_cont = "contact: "+cont+"\t"
                    compl_cur = "Current station: "+cur+"\t"
                    compl_gen = "Gender: "+gend+"\t"
                    compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                    msg.insert(tk.END, compll_msg)
                    msg.insert(tk.END,"\n" )
            if(name1!= name):
                msg.delete(0.0,END)
                err_msg="no record"
                msg.insert(tk.END,err_msg)

    search_but = Button(top3, text="search" , command = pol_search,font="fixedsys")
    search_but.grid(row =2, column= 1 )


    pol_home_button = Button(top3, text = "HOME",bg= "orange", command= top3.destroy,font="fixedsys")
    pol_home_button.grid(row= 2 , column = 2)

    f.close()
def search_crim():
    top4 = Toplevel()
    top4.title("SEARCH FOR CRIMINAL RECORDS")
    top4.config(background= "powder blue")
    crim_id_label  = Label(top4, text = "enter the id of criminal(optional)",font="fixedsys")
    crim_id_entry = Entry(top4)
    crim_id_label.grid(row = 0)
    crim_id_entry.grid(row = 0, column = 1)

    crim_name_label = Label(top4, text = "enter criminal name",font="fixedsys")
    crim_name_entry = Entry(top4)
    crim_name_label.grid(row = 1)
    crim_name_entry.grid(row = 1, column = 1)

    msg = Text(top4, width = 40, height = 10)
    msg.grid(row = 5, column =4,sticky = W)
    first_msg = "SEARCH RESULT APPEAR HERE"
    msg.insert(tk.END, first_msg)

    def crim_search():
        name=""
        last=0
        fields = list()
        compl_id = ""
        compl_name=""
        compl_add=""
        compl_cont=""
        compl_cur=""
        compl_gen=""
        compll_msg=""
        gend=""
        id2=0
        flag=0
        id = crim_id_entry.get()
        name1 = crim_name_entry.get()


        f = open("crimrec.txt","r")
        if(id):
            id1= int(id)
            for line in f:
                if(line == "*"+"\n"):
                    continue
                elif(line!="*"+"\n"):
                    fields = line.split("|")
                    bin_list = list()
                    dummy = fields[0]
                    ID = int(dummy)
                    bin_list.append(ID)
                    print((type(bin_list[0])))
                high = len(bin_list)-1
                print(high)
                low = 0
                while(high>=low):
                    mid = (low+high)//2
                    if (bin_list[mid]==id1):
                        flag=1
                        break
                    elif(bin_list[mid]<id1):
                        low= mid+1
                    elif(bin_list[mid]>id1):
                        high = mid-1
            f.close()
            f=open("crimrec.txt","r")
            l =list()
            if(flag==1):
                for line in f:
                    if(line=="*"+"\n"):
                        continue
                    elif(line!="*"+"\n"):
                        l = line.split("|")
                        print(l)
                        ID1 = l[0]
                        ID2 = int(ID1)
                        if(ID1==id):
                            msg.delete(0.0,END)
                            compl_id = "id :"+l[0]+"\t"
                            compl_name = "name: "+l[1]+"\t"
                            compl_add = "address: "+l[2]+"\t"
                            compl_cont = "contact: "+l[3]+"\t"
                            compl_cur = "Current jail/Status: "+l[4]+"\t"
                            compl_gen = "Gender: "+ gend+"\t"
                            compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                            msg.insert(tk.END, compll_msg)
            elif(flag==0):
                msg.delete(0.0,END)
                msg.insert(tk.END,"NO RECORD FOUND!")

        elif name1:
            count = 0
            for line in f:
                count = count+1
                if (name1+"|") not in line:
                    continue
                elif (name1+"|") in line:
                    fields = line.split("|" or "$")
                    id_1 = fields[0]
                    id2 = int(id_1)
                    name = fields[1]
                    addr = fields[2]
                    cont = fields[3]
                    cur = fields[4]
                    gen = fields[5]
                    msg.insert(tk.END,"\n")
                    compl_id = "id :"+id_1+"\t"
                    compl_name = "name: "+name+"\t"
                    compl_add = "address: "+addr+"\t"
                    compl_cont = "contact: "+cont+"\t"
                    compl_cur = "Current station: "+cur+"\t"
                    compl_gen = "Gender: "+gend+"\t"
                    compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                    msg.insert(tk.END, compll_msg+"\n")

            if(name1!= name):
                msg.delete(0.0,END)
                err_msg="no record"
                msg.insert(tk.END,err_msg)

    search_but = Button(top4, text="search" , command = crim_search,font="fixedsys")
    search_but.grid(row =2, column= 1 )

    crim_home_button = Button(top4, text = "HOME",bg= "orange", command= top4.destroy,font="fixedsys")
    crim_home_button.grid(row= 2 , column = 2)

    f.close()
def del_pol():
    top5 = Toplevel()
    top5.title("DELETE POLICE RECORD")
    top5.config(background = "tan1")
    pol_id_label = Label(top5, text="Enter police id",font="fixedsys")
    pol_id_entry = Entry(top5)
    pol_id_label.grid(row = 0)
    pol_id_entry.grid(row = 1, column = 1)

    msg = Text(top5, width = 40, height = 10)
    msg = Text(top5, width = 40, height = 10)
    msg.grid(row = 2, column =4,sticky = W)
    first_msg = "NOTIFICATION APPEARS HERE"
    msg.insert(tk.END, first_msg)

    def del_but():
        id = pol_id_entry.get()
        f = open("policerec.txt", "r")
        int_id = int(id)
        l = list()
        for line in f:
            if not line.startswith(id+"|"):
                msg.delete(0.0,END)
                msg.insert(tk.END,"Invalid ID")
        f.close()
        f = open("policerec.txt","r")
        for line in f:
            l.append(line)
        l[int_id-1]= "*"+"\n"
        f.close()
        f = open("policerec.txt","w")
        for i in range(0,len(l)):
            s = l[i]
            f.write(s)
        msg.delete(0.0,END)
        msg.insert(tk.END,"Record deleted")
        f.flush()
    delete_but = Button(top5, text = "Delete", command = del_but,font="fixedsys")
    delete_but.grid(row=3,column =3 )


    pol_home_button = Button(top5, text = "HOME",bg= "orange", command= top5.destroy,font="fixedsys")
    pol_home_button.grid(row= 3 , column = 4)

def del_crim():
    top6 = Toplevel()
    top6.title("DELETE CRIMINAL RECORD")
    top6.config(background="thistle")
    crim_id_label = Label(top6, text="Enter criminal id",font="fixedsys")
    crim_id_entry = Entry(top6)
    crim_id_label.grid(row = 0)
    crim_id_entry.grid(row = 1, column = 1)

    msg = Text(top6, width = 40, height = 10)
    msg = Text(top6, width = 40, height = 10)
    msg.grid(row = 2, column =4,sticky = W)
    first_msg = "NOTIFICATION APPEARS HERE"
    msg.insert(tk.END, first_msg)

    def del_but():
        id = crim_id_entry.get()
        f = open("crimrec.txt", "r")
        int_id = int(id)
        l = list()
        for line in f:
            if not line.startswith(id+"|"):
                msg.delete(0.0,END)
                msg.insert(tk.END,"Invalid ID")
        f.close()
        f = open("crimrec.txt","r")
        for line in f:
            l.append(line)
        l[int_id-1]= "*"+"\n"
        f.close()
        f = open("crimrec.txt","w")
        for i in range(0,len(l)):
            s = l[i]
            f.write(s)
        msg.delete(0.0,END)
        msg.insert(tk.END,"Record deleted")
        f.flush()
    delete_but = Button(top6, text = "Delete", command = del_but,font="fixedsys")
    delete_but.grid(row=3,column =3 )

    crim_home_button = Button(top6, text = "HOME",bg= "orange", command= top6.destroy,font="fixedsys")
    crim_home_button.grid(row= 3 , column = 4)


def mod_pol():
    top7 = Toplevel()
    top7.title("MODIFY POLICE RECORD")
    mod_instr = Label(top7, text = "Please enter old values if no changes are required",font="Fixedsys")
    mod_instr.grid(row = 0,column=1)
    pol_id_label  = Label(top7,text = "Enter police ID to be modified",font="SansSerif")
    pol_id_entry = Entry(top7)
    pol_id_label.grid(row= 1, column =1 )
    pol_id_entry.grid(row = 2, column = 1)

    def srch():
        name=""
        id_1=""
        last=0
        fields = list()
        compl_id = ""
        compl_name=""
        compl_add=""
        compl_cont=""
        compl_cur=""
        compl_gen=""
        compll_msg=""
        gend=""
        id2=0
        id = pol_id_entry.get()

        f = open("policerec.txt","r")
        if(id):
            for line in f:
                if line.startswith(id+"|"):
                    fields = line.split("|" or "$")
                    id_1 = fields[0]
                    name = fields[1]
                    addr = fields[2]
                    cont = fields[3]
                    cur = fields[4]
                    gen = fields[5]
                    if (gen is "1$"):
                        gend = "Male"
                    elif(gen is"2$"):
                        gend = "Female"
                    msg.delete(0.0,END)
                    compl_id = "id :"+id_1+"\t"
                    compl_name = "name: "+name+"\t"
                    compl_add = "address: "+addr+"\t"
                    compl_cont = "contact: "+cont+"\t"
                    compl_cur = "Current station: "+cur+"\t"
                    compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                    msg.insert(tk.END, compll_msg)

            if(id_1 !=id):
                msg.delete(0.0,END)
                err_msg = "no record found"
                msg.insert(tk.END,err_msg)
    srch_but = Button(top7, text = "Search", command = srch)
    srch_but.grid(row =3 , column= 1 )
    pol_name_label = Label(top7, text= "enter name of the police",font="SansSerif")
    pol_name_entry= Entry(top7)
    pol_name_label.grid(row=4)
    pol_name_entry.grid(row= 4, column = 1)

    pol_addr_label = Label(top7, text= "enter police address",font="SansSerif")
    pol_addr_entry= Entry(top7)
    pol_addr_label.grid(row=5)
    pol_addr_entry.grid(row= 5, column = 1)


    pol_contact_label = Label(top7, text= "enter contact no.",font="SansSerif")
    pol_contact_entry= Entry(top7)
    pol_contact_label.grid(row=6)
    pol_contact_entry.grid(row= 6, column = 1)


    pol_cur_label = Label(top7, text= "enter current station",font="SansSerif")
    pol_cur_entry= Entry(top7)
    pol_cur_label.grid(row=7)
    pol_cur_entry.grid(row= 7, column = 1)

    gend = IntVar()
    male = Radiobutton(top7, text = "Male", variable = gend, value =1)
    female = Radiobutton(top7 , text = "Female" , variable = gend , value = 2)
    male.grid(row = 8, column = 1)
    female.grid(row=8,column=2)

    msg = Text(top7, width = 40, height = 10)
    msg.grid(row = 9, column =4,sticky = W)
    first_msg = "SEARCH RESULTS APPEAR HERE"
    msg.insert(tk.END, first_msg)
    def modify():
        id = pol_id_entry.get()
        s =""
        new_id=""
        new_name=""
        new_addr = ""
        new_cont=""
        new_cur = ""
        new_gen=""
        feed = ""
        f = open("policerec.txt", "r")
        int_id = int(id)
        l = list()
        for line in f:
            l.append(line)
        s = l[int_id-1]
        fields = s.split("|")
        new_id = pol_id_entry.get()
        new_name = pol_name_entry.get()
        new_addr = pol_addr_entry.get()
        new_cont = pol_contact_entry.get()
        new_cur = pol_cur_entry.get()
        new_gen  = str(gend.get())
        s = new_id+"|"+new_name+"|"+new_addr+"|"+new_cont+"|"+new_cur+"|"+new_gen+"$"+"\n"
        l[int_id-1] = s
        f.close()
        f = open("policerec.txt","w")
        for i in range(0,len(l)):
            feed = l[i]
            f.write(feed)
        f.close()
        msg.delete(0.0,END)
        msg.insert(tk.END,"Record modified")

    mod_but = Button(top7, text= "Modify",command = modify)
    mod_but.grid(row = 9, column = 1)

    pol_home_button = Button(top7, text = "HOME",bg= "orange", command= top7.destroy)
    pol_home_button.grid(row= 9 , column = 2)
def mod_crim():
    top8 = Toplevel()
    top8.title("MODIFY CRIMINAL RECORD")
    mod_instr = Label(top8, text = "Please enter old values if no changes are required",font="CourierNew")
    mod_instr.grid(row = 0,column=1)
    crim_id_label  = Label(top8,text = "Enter criminal ID to be modified",font="CourierNew")
    crim_id_entry = Entry(top8)
    crim_id_label.grid(row= 1, column =1 )
    crim_id_entry.grid(row = 2, column = 1)

    def crim_search():
        name=""
        id_1=""
        last=0
        fields = list()
        compl_id = ""
        compl_name=""
        compl_add=""
        compl_cont=""
        compl_cur=""
        compl_gen=""
        compll_msg=""
        gend=""
        id2=0
        id = crim_id_entry.get()
        name1 = crim_name_entry.get()


        f = open("crimrec.txt","r")
        if(id):
            for line in f:
                if line.startswith(id+"|"):
                    fields = line.split("|" or "$")
                    id_1 = fields[0]
                    name = fields[1]
                    addr = fields[2]
                    cont = fields[3]
                    cur = fields[4]
                    gen = fields[5]
                    if (gen is "1$"):
                        gend = "Male"
                    elif(gen is"2$"):
                        gend = "Female"
                    msg.delete(0.0,END)
                    compl_id = "id :"+id_1+"\t"
                    compl_name = "name: "+name+"\t"
                    compl_add = "address: "+addr+"\t"
                    compl_cont = "contact: "+cont+"\t"
                    compl_cur = "Current station/Status: "+cur+"\t"
                    compll_msg = compl_id+compl_name+compl_add+compl_cont+compl_cur+"\n"
                    msg.insert(tk.END, compll_msg)

            if(id_1 !=id):
                msg.delete(0.0,END)
                err_msg = "no record found"
                msg.insert(tk.END,err_msg)

    srch_but = Button(top8, text = "Search", command = crim_search)
    srch_but.grid(row =3 , column= 1 )
    crim_name_label = Label(top8, text= "enter name of the criminal",font="CourierNew")
    crim_name_entry= Entry(top8)
    crim_name_label.grid(row=4)
    crim_name_entry.grid(row= 4, column = 1)

    crim_addr_label = Label(top8, text= "enter criminal address",font="CourierNew")
    crim_addr_entry= Entry(top8)
    crim_addr_label.grid(row=5)
    crim_addr_entry.grid(row= 5, column = 1)


    crim_contact_label = Label(top8, text= "enter contact no.",font="CourierNew")
    crim_contact_entry= Entry(top8)
    crim_contact_label.grid(row=6)
    crim_contact_entry.grid(row= 6, column = 1)


    crim_cur_label = Label(top8, text= "enter current Jail/status",font="CourierNew")
    crim_cur_entry= Entry(top8)
    crim_cur_label.grid(row=7)
    crim_cur_entry.grid(row= 7, column = 1)

    gend = IntVar()
    male = Radiobutton(top8, text = "Male", variable = gend, value =1)
    female = Radiobutton(top8 , text = "Female" , variable = gend , value = 2)
    male.grid(row = 8, column = 0)
    female.grid(row=8,column=1)

    msg = Text(top8, width = 40, height = 10)
    msg.grid(row = 9, column =4,sticky = W)
    first_msg = "SEARCH RESULTS APPEAR HERE"
    msg.insert(tk.END, first_msg)

    def modify():
        id = crim_id_entry.get()
        s =""
        new_id=""
        new_name=""
        new_addr = ""
        new_cont=""
        new_cur = ""
        new_gen=""
        feed = ""
        f = open("crimrec.txt", "r")
        int_id = int(id)
        l = list()
        for line in f:
            l.append(line)
        s = l[int_id-1]
        fields = s.split("|")
        new_id = crim_id_entry.get()
        new_name = crim_name_entry.get()
        new_addr = crim_addr_entry.get()
        new_cont = crim_contact_entry.get()
        new_cur = crim_cur_entry.get()
        new_gen  = str(gend.get())
        s = new_id+"|"+new_name+"|"+new_addr+"|"+new_cont+"|"+new_cur+"|"+new_gen+"$"+"\n"
        l[int_id-1] = s
        f.close()
        f = open("crimrec.txt","w")
        for i in range(0,len(l)):
            feed = l[i]
            f.write(feed)
        f.close()
        msg.delete(0.0,END)
        msg.insert(tk.END,"Record modified")

    mod_but = Button(top8, text= "Modify",command = modify,font="CourierNew")
    mod_but.grid(row = 10, column = 1)

    pol_home_button = Button(top8, text = "HOME",bg= "orange", command= top8.destroy,font="CourierNew")
    pol_home_button.grid(row= 10 , column = 2)

def disp_pol():
    top9 =Toplevel()
    top9.title= "Display police records"
    top9.geometry("400x300")

    msg = Text(top9, width = 120, height = 40)
    msg.grid(row = 0)
    first_msg = "\tID\t\tNAME\t\t\tADDRESS\t\t\tCONTACT\t\t\tCURRENT STATION\n"
    next_msg =first_msg+("\t________________________________________________________________________________________________________\n")
    msg.insert(tk.END, next_msg)

    def display():
        f = open("policerec.txt","r")
        for line in f:
            if (line == "*"+"\n"):
                continue
            elif(line != "*"+"\n"):
                l = line.split("|")
                id = l[0]
                name = l[1]
                adr = l[2]
                cont = l[3]
                cur= l[4]
                compmsg = "\t"+id+"\t\t"+name+"\t\t\t"+adr+"\t\t\t"+cont+"\t\t\t"+cur+"\n"
                msg.insert(tk.END, compmsg)
    disp_but = Button(top9, text = "Display records", command = display)
    disp_but.grid(row = 1)


    pol_home_button = Button(top9, text = "HOME",bg= "orange", command= top9.destroy)
    pol_home_button.grid(row= 1 , column = 1)
    f.close()

def disp_crim():
    top10 =Toplevel()
    top10.title= "Display criminal records"
    top10.geometry("400x300")

    msg = Text(top10, width = 120, height = 40)
    msg.grid(row = 0)
    first_msg = "\tID\t\tNAME\t\t\tADDRESS\t\t\tCONTACT\t\t\tCURRENT JAIL/STATUS\n"
    next_msg =first_msg+("\t________________________________________________________________________________________________________\n")
    msg.insert(tk.END, next_msg)

    def display():
        f = open("crimrec.txt","r")
        for line in f:
            if ((line == "*"+"\n") or (line=="\n")):
                continue
            elif(line != "*"+"\n"):
                l = line.split("|")
                id = l[0]
                name = l[1]
                adr = l[2]
                cont = l[3]
                cur= l[4]
                compmsg = "\t"+id+"\t\t"+name+"\t\t\t"+adr+"\t\t\t"+cont+"\t\t\t"+cur+"\n"
                msg.insert(tk.END, compmsg)
    disp_but = Button(top10, text = "Display records", command = display)
    disp_but.grid(row = 1)
    pol_home_button = Button(top10, text = "HOME",bg= "orange", command= top10.destroy)
    pol_home_button.grid(row= 2 , column = 1)

    f.close()

root = Tk()
root.title("POLICE STATION MANAGEMENT SYSTEM")
root.geometry("900x600")

menu = Menu(root)
root.config(menu = menu)

Submenu =Menu(menu)
menu.add_cascade(label = "POLICE RECORD MANAGEMENT", menu = Submenu,font = "ComicSans")
Submenu.add_command(label = "Insert police record", command= insert_pol)
Submenu.add_separator()
Submenu.add_command(label = "Search police record", command= search_pol)
Submenu.add_separator()
Submenu.add_command(label = "Delete police record", command= del_pol)
Submenu.add_separator()
Submenu.add_command(label = "Modify police record", command= mod_pol)
Submenu.add_separator()
Submenu.add_command(label = "Display police record", command= disp_pol)

crim_menu  = Menu(menu)
menu.add_cascade(label = "CRIMINAL RECORD MANAGEMENT", menu=crim_menu)
crim_menu.add_command(label = "Insert criminal record", command= insert_crim)
crim_menu.add_separator()
crim_menu.add_command(label = "Search criminal record", command= search_crim)
crim_menu.add_separator()
crim_menu.add_command(label = "Delete criminal record", command= del_crim)
crim_menu.add_separator()
crim_menu.add_command(label = "Modify criminal record", command= mod_crim)
crim_menu.add_separator()
crim_menu.add_command(label = "Display criminal record", command= disp_crim)




photo1 = PhotoImage (file = "po.png")
photolabele1 = Label(image = photo1)
photolabele1.pack(side = TOP)


button9 = Button(root, text = "Save", bg= "grey",command= root.destroy)
button9.pack(side =TOP,fill = X)

root.mainloop()