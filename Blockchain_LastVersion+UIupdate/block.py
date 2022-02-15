from cProfile import label
from cgitb import text
from ctypes import alignment
import json
import os
import hashlib
import datetime
from tkinter import *

blockchain_dir = "Blockchain_LastVersion/blockchain/"

# function เพื่อคำนวณค่า hash ของ block
def get_hash(prev_block):
    with open(blockchain_dir+prev_block,'rb')as f: # เปิดไฟล์ของ previous block
        content = f.read()                         # อ่านไฟล์แล้วเก็บเป็นชื่อว่า content
    return hashlib.sha256(content).hexdigest()     # ทำการ hash content นั้น

def check_update():
    blocks_count = len(os.listdir(blockchain_dir))
    with open(blockchain_dir + "11") as f:
            block = json.load(f) 

    prev_filename =  block.get("prev_block").get("prev_filename")
    if (prev_filename == "11"):
        return 0
    else:
        return 1
# function เพื่อตรวจสอบความถูกต้องของ block
def check_integrity():
    files = sorted(os.listdir(blockchain_dir),key=lambda x: int(x)) # file ทั้งหมด
    
    results = []
    
    for file in files[1:]: # วนลูปตั้งแต่ file แรกจนถึง file สุดท้าย
        with open(blockchain_dir + file) as f: # ไล่เปิดไฟล์เริ่มตั้งแต่ file แรก
            block = json.load(f)               # ให้ block เป็นตัว json ของไฟล์นั้น
        
        prev_hash = block.get("prev_block").get("prev_hash") # get ค่า hash จาก previous block
        prev_filename =  block.get("prev_block").get("prev_filename") # get ค่า filename จาก previous block
        
        actual_hash = get_hash(prev_filename) # หา hash ของ previous file
        
        if prev_hash == actual_hash: 
            res = "Ok"
        else:
            res = "was Changed"
        
        print(f"Block {prev_filename}:{res}")
        results.append({'block':prev_filename,'result':res})
    return results

# function การเขียน block เพิ่มลงไป           
def write_block(day,date,rank1,rank2,rank3,rank4,rank5,rank6,rank7,rank8,rank9):
    
    blocks_count = len(os.listdir(blockchain_dir)) # นับจำนวน block ก่อนหน้า (ตอนนี้ที่มี)
    prev_block = str(blocks_count) # ให้ previous block เป็น string จำนวนของ block ก่อนหน้า
    index = blocks_count+1
    timestamp = str(datetime.datetime.now())
    data = {                       # กำหนดให้ data ใน block มีอะไรบ้าง
        "index":index,
        "timestamp":timestamp,
        "data" :{
          "day": day,
          "date":date, 
        "rank1": rank1,
        "rank2": rank2,
        "rank3": rank3,
        "rank4": rank4,
        "rank5": rank5,
        "rank6": rank6, 
        "rank7": rank7,
        "rank8": rank8,
        "rank9": rank9,   
        },        
        "prev_block":{
        "prev_hash":get_hash(prev_block),
        "prev_filename": prev_block
        }
    }
    
    current_block = blockchain_dir + str(blocks_count+1) # กำหนดให้ชื่อ current block เป็นชื่อ block เดิม +1
    
    with open(current_block,"w") as f:      # เขียนไฟล์ current block ด้วย data
        json.dump(data, f,indent=4,ensure_ascii=False)
        f.write("\n")

def main():
    blocks_count = len(os.listdir(blockchain_dir))
    if blocks_count==1 :
        #1
        write_block(day="1",date="01/29/2022",rank1="King Of Gamers Club",rank2="PSG Esports",rank3="Buriram United Esports",rank4="KFC X Talon",rank5="Goldcity Esports",rank6="Earena",rank7="Bacon Time",rank8="Valencia CF Esports",rank9="Evos Esports")
        #2
        write_block(day="2",date="01/30/2022",rank1="PSG Esports",rank2="Buriram United Esports",rank3="King Of Gamers Club",rank4="Earena",rank5="KFC X Talon",rank6="Evos Esports",rank7="Goldcity Esports",rank8="Bacon Time",rank9="Valencia CF Esports")
        #3
        write_block(day="3",date="02/03/2022",rank1="PSG Esports",rank2="Buriram United Esports",rank3="King Of Gamers Club",rank4="Earena",rank5="Bacon Time",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #4
        write_block(day="4",date="02/04/2022",rank1="PSG Esports",rank2="Buriram United Esports",rank3="King Of Gamers Club",rank4="Earena",rank5="Bacon Time",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #5
        write_block(day="5",date="02/05/2022",rank1="King Of Gamers Club",rank2="PSG Esports",rank3="Buriram United Esports",rank4="Earena",rank5="Bacon Time",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #6
        write_block(day="6",date="02/06/2022",rank1="PSG Esports",rank2="King Of Gamers Club",rank3="Earena",rank4="Bacon Time",rank5="Buriram United Esports",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #7
        write_block(day="7",date="02/07/2022",rank1="Earena",rank2="PSG Esports",rank3="King Of Gamers Club",rank4="Bacon Time",rank5="Buriram United Esports",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #8
        write_block(day="8",date="02/08/2022",rank1="Earena",rank2="PSG Esports",rank3="King Of Gamers Club",rank4="Bacon Time",rank5="Buriram United Esports",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #9
        write_block(day="9",date="02/10/2022",rank1="Earena",rank2="PSG Esports",rank3="King Of Gamers Club",rank4="Bacon Time",rank5="Buriram United Esports",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")
        #10
        write_block(day="10",date="02/11/2022",rank1="Earena",rank2="Bacon Time",rank3="Buriram United Esports",rank4="PSG Esports",rank5="King Of Gamers Club",rank6="KFC X Talon",rank7="Goldcity Esports",rank8="Evos Esports",rank9="Valencia CF Esports")

    #check_integrity()
     
    pass

if __name__ == '__main__':
    main()
    
   
# GUI
def main_screen():
    screen = Tk()
    screen.title("Blockchain Project")
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")
    
    lblTitle = Label(text="Blockchain Project",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    lblTitle.pack(pady=50)
    
    bordercolor = Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()
    
    mainframe = Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)
    
    def searchBlock():
        mdSerchBlock=Toplevel(screen)
        mdSerchBlock.title("Search Block")
        mdSerchBlock.geometry("1280x720+150+80")
        mdSerchBlock.configure(bg="#d7dae2")
        mdSerchBlock.resizable(False,False)
        
        block_no = StringVar()
        
        lblTitle = Label(mdSerchBlock,text="Search Block",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
        lblTitle.pack(pady=50)
        bordercolor = Frame(mdSerchBlock,bg="black",width=800,height=400)
        bordercolor.pack()
    
        mainframe = Frame(bordercolor,bg="#d7dae2",width=800,height=400)
        mainframe.pack(padx=20,pady=20)
        
        def search():
            bno = block_no.get()
            if ((bno=="all")or(bno=="All")or(bno=="ALL")):
                blocks_count = len(os.listdir(blockchain_dir)) 
                data = ""
                for i in range(1,blocks_count+1):
                    data_block = {}
                    with open(f"Blockchain_LastVersion/blockchain/{i}",'r')as f: 
                        content = f.read()

                    temp = str(content)
                    data_block = temp.split("\n")
                    for f in range(1,20):
                        if (f==15):
                            data = data
                        elif (f==19 and i!=blocks_count):
                            data = data+"\n\n\n"
                        elif ((f>=4 and f<=14) or (f>=17 and f<=18)):
                            data = data+"\n     "+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                        elif (f==1):
                            data = data+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                        else :
                            data = data+"\n"+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                text_box.insert(1.0,data)
            else :
                data_block = {}
                with open(f"Blockchain_LastVersion/blockchain/{bno}",'r')as f: 
                    content = f.read()
                
                temp = str(content)
                data_block = temp.split("\n")
                data = ""
                for f in range(1,21):
                    if (f==15):
                        data = data
                    elif ((f>=4 and f<=14) or(f>=17)):
                        data = data+"\n     "+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                    elif (f==1):
                        data = data+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                    else :
                        data = data+"\n"+data_block[f].lstrip().replace("\"","").replace(",","").replace("{","").replace("}","")
                text_box.insert(1.0,data)



        def clear():
            entry_block.delete(0,END)
            text_box.delete('1.0', END)
        
        
        Label(mainframe,text="Please Enter Number of the Block :",font=("arial",15),bg="#d7dae2").place(x=50,y=30)
        entry_block = Entry(mainframe,textvariable=block_no,width=12,bd=2,font=("arial",15))
        entry_block.place(x=390,y=30)
    
        Button(mainframe,text="Search",height="2",width=12,bg="#4CCE2E",fg="black",bd=0,command=search).place(x=540,y=26)
        Button(mainframe,text="Clear",height="2",width=12,bg="#AEB6BF",fg="black",bd=0,command=clear).place(x=640,y=26)
        
        text_box = Text(mainframe,height=15,width=83,padx=15,pady=15)
        text_box.place(x=50,y=100)
        
        screen.mainloop()
    
    def addBlock():
        mdAddBlock=Toplevel(screen)
        mdAddBlock.title("Add Block")
        mdAddBlock.geometry("1280x720+150+80")
        mdAddBlock.configure(bg="#d7dae2")
        mdAddBlock.resizable(False,False)
        
        day_in = StringVar()
        date_in = StringVar()
        rank1_in = StringVar()
        rank2_in = StringVar()
        rank3_in = StringVar()
        rank4_in = StringVar()
        rank5_in = StringVar()
        rank6_in = StringVar()
        rank7_in = StringVar()
        rank8_in = StringVar()
        rank9_in = StringVar()
        
        lblTitle = Label(mdAddBlock,text="Add Block",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
        lblTitle.pack(pady=50)
        bordercolor = Frame(mdAddBlock,bg="black",width=800,height=400)
        bordercolor.pack()
    
        mainframe = Frame(bordercolor,bg="#d7dae2",width=800,height=400)
        mainframe.pack(padx=20,pady=20)
        
        def add():
             write_block(day=day_in.get(),date=date_in.get(),rank1=rank1_in.get(),rank2=rank2_in.get(),rank3=rank3_in.get(),rank4=rank4_in.get(),rank5=rank5_in.get(),rank6=rank6_in.get(),rank7=rank7_in.get(),rank8=rank8_in.get(),rank9=rank9_in.get())
        def clear():
            entry_block1.delete(0,END)
            entry_block2.delete(0,END)
            entry_block3.delete(0,END)
            entry_block4.delete(0,END)
            entry_block5.delete(0,END)
            entry_block6.delete(0,END)
            entry_block7.delete(0,END)
            entry_block8.delete(0,END)
            entry_block9.delete(0,END)
            entry_block10.delete(0,END)
            entry_block11.delete(0,END)
            
        Label(mainframe,text="Please Enter Data :",font=("arial",15),bg="#d7dae2").place(x=50,y=30)
        Label(mainframe,text="Day",font=("arial",15),bg="#d7dae2").place(x=50,y=70)
        entry_block1 = Entry(mainframe,textvariable=day_in,width=22,bd=2,font=("arial",15))
        entry_block1.place(x=120,y=70)
        Label(mainframe,text="Date",font=("arial",15),bg="#d7dae2").place(x=400,y=70)
        entry_block2 = Entry(mainframe,textvariable=date_in,width=22,bd=2,font=("arial",15))
        entry_block2.place(x=450,y=70)
        Label(mainframe,text="Rank1",font=("arial",15),bg="#d7dae2").place(x=50,y=110)
        entry_block3 = Entry(mainframe,textvariable=rank1_in,width=22,bd=2,font=("arial",15))
        entry_block3.place(x=120,y=110)
        Label(mainframe,text="Rank2",font=("arial",15),bg="#d7dae2").place(x=380,y=110)
        entry_block4 = Entry(mainframe,textvariable=rank2_in,width=22,bd=2,font=("arial",15))
        entry_block4.place(x=450,y=110)
        Label(mainframe,text="Rank3",font=("arial",15),bg="#d7dae2").place(x=50,y=150)
        entry_block5 = Entry(mainframe,textvariable=rank3_in,width=22,bd=2,font=("arial",15))
        entry_block5.place(x=120,y=150)
        Label(mainframe,text="Rank4",font=("arial",15),bg="#d7dae2").place(x=380,y=150)
        entry_block6 = Entry(mainframe,textvariable=rank4_in,width=22,bd=2,font=("arial",15))
        entry_block6.place(x=450,y=150)
        Label(mainframe,text="Rank5",font=("arial",15),bg="#d7dae2").place(x=50,y=190)
        entry_block7 = Entry(mainframe,textvariable=rank5_in,width=22,bd=2,font=("arial",15))
        entry_block7.place(x=120,y=190)
        Label(mainframe,text="Rank6",font=("arial",15),bg="#d7dae2").place(x=380,y=190)
        entry_block8 = Entry(mainframe,textvariable=rank6_in,width=22,bd=2,font=("arial",15))
        entry_block8.place(x=450,y=190)
        Label(mainframe,text="Rank7",font=("arial",15),bg="#d7dae2").place(x=50,y=230)
        entry_block9 = Entry(mainframe,textvariable=rank7_in,width=22,bd=2,font=("arial",15))
        entry_block9.place(x=120,y=230)
        Label(mainframe,text="Rank8",font=("arial",15),bg="#d7dae2").place(x=380,y=230)
        entry_block10 = Entry(mainframe,textvariable=rank8_in,width=22,bd=2,font=("arial",15))
        entry_block10.place(x=450,y=230)
        Label(mainframe,text="Rank9",font=("arial",15),bg="#d7dae2").place(x=50,y=270)
        entry_block11 = Entry(mainframe,textvariable=rank9_in,width=22,bd=2,font=("arial",15))
        entry_block11.place(x=120,y=270)
        
        Button(mainframe,text="Add",height="2",width=22,bg="#4CCE2E",fg="black",bd=0,command=add).place(x=160,y=325)
        Button(mainframe,text="Clear",height="2",width=22,bg="#AEB6BF",fg="black",bd=0,command=clear).place(x=500,y=325)
        
        screen.mainloop()
    
    def checkBlock():
        mdCheckBlock=Toplevel(screen)
        mdCheckBlock.title("Check Block")
        mdCheckBlock.geometry("1280x720+150+80")
        mdCheckBlock.configure(bg="#d7dae2")
        mdCheckBlock.resizable(False,False)
        
        
        lblTitle = Label(mdCheckBlock,text="Check Block",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
        lblTitle.pack(pady=50)
        bordercolor = Frame(mdCheckBlock,bg="black",width=800,height=400)
        bordercolor.pack()
    
        mainframe = Frame(bordercolor,bg="#d7dae2",width=800,height=400)
        mainframe.pack(padx=20,pady=20)
        
        def check():
            res = check_integrity()

            temp = str(res)
            data_res = temp.split(", {")
            data = ""
            for i in range(0,9):
                if (i==0):
                    data = data+data_res[i].lstrip().replace("\'","").replace(",","").replace("{","").replace("}","").replace("[","")
                else :
                    data = data+"\n"+data_res[i].lstrip().replace("\'","").replace(",","").replace("{","").replace("}","")
            text_box.insert(1.0,data)

        def clear():
            text_box.delete('1.0', END)
        
        Button(mainframe,text="Check Integrity Now!!!",height="2",width=23,bg="#4CCE2E",fg="black",bd=0,command=check).place(x=250,y=20)
        Button(mainframe,text="Clear",height="2",width=12,bg="#AEB6BF",fg="black",bd=0,command=clear).place(x=450,y=20)
        
        text_box = Text(mainframe,height=15,width=83,padx=15,pady=15)
        text_box.place(x=50,y=100)
        
        screen.mainloop()
    
    Label(mainframe,text="This is Blockchain Project Develope by :",font=("arial",15),bg="#d7dae2").place(x=10,y=30)
    Label(mainframe,text="1. B6201982 Tanakorn Sookkul",font=("arial",15),bg="#d7dae2").place(x=10,y=70)
    Label(mainframe,text="2. B6220730 Chawarat Narit",font=("arial",15),bg="#d7dae2").place(x=10,y=110)
    Label(mainframe,text="You can choose three mode for Search Block , Add Block and Check Block",font=("arial",15),bg="#d7dae2").place(x=10,y=150)
    
    Button(mainframe,text="Search Block",height="5",width=23,bg="#ed3833",fg="black",bd=0,command=searchBlock).place(x=100,y=250)
    Button(mainframe,text="Add Block",height="5",width=23,bg="#1089ff",fg="black",bd=0,command=addBlock).place(x=300,y=250)
    Button(mainframe,text="Check Block",height="5",width=23,bg="#00bd56",fg="black",bd=0,command=checkBlock).place(x=500,y=250)
    screen.mainloop()

main_screen()