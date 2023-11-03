from tkinter import * 
from tkinter.font import Font
import tkinter as tk
from time import strftime
from datetime import date
from time import sleep 

class ui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.title('CLOCK')
        self.iconphoto(False,tk.PhotoImage(file="icon3.png"))
        self.maxsize(width=500,height=150)
        self.config(background="#616161")
    



root=ui()
option=Frame(root,background="#616161",border=6)
option.pack(side=LEFT,fill=Y)
enter=Frame(root,background="#616161",border=6)
enter.pack(anchor=CENTER,fill=X)
ds=Font(family="Gill Sans MT",size=50)
datefont=Font(family="Gill Sans MT",size=25)
im=PhotoImage(file="timericon.png")
im2=PhotoImage(file="timeicon.png")

global l
def clear_frame(event=None):
   for widgets in enter.winfo_children():
      widgets.destroy()
   if event!=None :
        timer2(None)

def time1(e=None):
        global inp
        global enter
        global l
        global ld
        global start
        global disp
        clear_frame()
        datee=date.today()
        l=Label(enter,font=ds,background="#616161",foreground="#ff7f27")
        l.pack()  
        ld=Label(enter,font=datefont,background="#616161",foreground="#ff7f27",text=f'{datee.strftime("%B %d, %Y %A")}')
        ld.pack(anchor=CENTER)
        def time():
                
                String = strftime('%I:%M:%S %p')
                l.config(text = String)
                l.after(1000,time)
                
        time()
time1()


def magic(numList):
        s = ''.join(map(str, numList))
        try:
            return int(s)
        except:
            return 0


def valueevalv(enteredtime):
    var=[]

    for i in range(len(enteredtime)):
            try:
                if enteredtime[0]!=" " :
                    if enteredtime[0]==":":
                        enteredtime.pop(0)
                        break
                    var.append(enteredtime[0]) 
            except:
                pass
            enteredtime.pop(0)

    intvar=magic(var)
    return intvar



def counter(e):
    global inp
    global start
    global disp
    
    timein=list(inp.get())
    clear_frame()
    disp=Label(enter,font=ds,background="#616161",foreground="#ff7f27",height=4)
    disp.pack(side=LEFT,padx=50,pady=0)
    
    stop=Button(enter,text="STOP",width=7,height=1,border=0,bg="#ff7f27",activebackground="#616161")
    stop.bind("<Button-1>",clear_frame)
    stop.pack(anchor=NW,padx=4)
    # stop=Button(enter,text="STOP",background="#ff7f27")
    # stop.bind("<Button-1>",clear_frame)
    # stop.pack(anchor=W)
    
    
    hr=valueevalv(timein)
    mi=valueevalv(timein)
    sec=valueevalv(timein)
    if hr==0 and mi==0 and sec==0:
        timer2(None)
    if sec>=60:
        mi=mi+int(sec/60)
        sec=sec%60
    if mi>=60:
        hr=hr+int(mi/60)
        mi=mi%60
    
    ts=hr*3600+mi*60+sec

    for i in range(ts):
        try:
           disp.config(text=f"{str(hr).zfill(2)}:{str(mi).zfill(2)}:{str(sec).zfill(2)}")
           disp.update()
        except:
            print("terminated")
            break
        sleep(1)
        #various cases to handle ino min and second
        if (sec==0 and mi!=0):
            mi-=1
            sec=60
        elif(hr!=0 and (mi==0 or sec==0)):
            hr-=1
            mi=59
            sec=60
        elif mi==0 and hr!=0:
            hr-=1
            mi=59
        elif ts==0 or (hr==0 and mi==0 and sec==0):
            break
        sec-=1
        ts-=1
      

def timer2(e):
    global inp
    global l
    global count
    global start
    clear_frame()
    inp=tk.Entry(enter) 
    count=0
    start=Button(enter,text="START",width=6,height=1,border=0,bg="#ff7f27",activebackground="#616161")
    start.bind("<Button-1>",counter)
    start.pack(anchor=NE,padx=40)

    def cursor(e):
        global count
        temp=list(inp.get())
        if count==1:
            temp.remove(":")
        elif count>1:
            return
        for i in range(len(temp)):
            if temp[i]==":":
                inp.icursor(i+3)
                count+=1
                break
            
        
    def only_numbers(char):
        if char.isdigit() or char==" ":
            return True
        else:
            return False
    validation = root.register(only_numbers)
    inp.insert(10,"      ")
    inp.insert(20,":")
    inp.insert(10,"     ") 
    inp.insert(50,":")
    
    inp.config(font=ds,width=13,border=1,background="#616161",foreground="#ff7f27",validate="key", validatecommand=(validation,"%S"))
    inp.pack(side=LEFT,pady=11)
    root.bind("<Return>",cursor)

 
clock=Button(option,image=im2,width=56,height=56,border=0,bg="black",activebackground="#616161")
clock.bind("<Button-1>",time1)
clock.pack(side=TOP,)

timer=Button(option,image=im,width=53,height=57,border=0,background="#616161",activebackground="#616161")
timer.bind("<Button-1>",timer2)
timer.pack(side=TOP,pady=7)

        
root.mainloop()

