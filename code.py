from tkinter import * 
from tkinter.font import Font
import tkinter as tk

from time import strftime

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
im=PhotoImage(file="timericon.png")
im2=PhotoImage(file="timeicon.png")

# l=Label(enter,font=ds,background="#616161",foreground="#ff7f27")
# l.pack()
global l
def time1(e):
        global ino
        global enter
        global l
        try:
            ino.destroy()
        except:
               pass
        l=Label(enter,font=ds,background="#616161",foreground="#ff7f27")
        l.pack()    
        def time():
                String = strftime('%I:%M:%S %p')
                l.config(text = String)
                print("x")
                l.after(1000,time)
        time()

def magic(numList):
        s = ''.join(map(str, numList))
        return int(s)

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
    time=list(inp.get())
    hr=valueevalv(time)
    mi=valueevalv(time)
    sec=valueevalv(time)
    if sec>=60:
        mi=mi+int(sec/60)
        sec=sec%60
        print(sec)
    if mi>=60:
        hr=hr+int(mi/60)
        mi=mi%60
    print(hr,mi,sec)
      

def timer2(e):
    global inp
    global l
    global count
    try:
        l.destroy()
    except:
        pass
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
            count=0
        for i in range(len(temp)):
            if temp[i]==":":
                inp.icursor(i+2)
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












# user=input("Enter the duration of timer (hh:mm:ss):")

# value=user.split(":")
# h=int(value[0])
# m=int(value[1])
# s=int(value[2])
#
# #main function
# def counter(h,m,s):
#     hs=h*3600
#     ms=m*60
#     ts=hs+ms+s#total no. of seconds
#     while True:
#         print(f" COUNTDOWN {h}:{m}:{s} ",end="\r")
#         time.sleep(1)
#         #various cases to handle ino min and second
#         if (s==0 and m!=0):
#             m-=1
#             s=60
#         elif(h!=0 and (m==0 or s==0)):
#             h-=1
#             m=59
#             s=60
#         elif m==0 and h!=0:
#             h-=1
#             m=59
#         elif ts==0 or (h==0 and m==0 and s==0):
#             break
#         s-=1
#         ts-=1

# y=counter(h,m,s)
# print('\nTIMESUP!!!')


# # print(y)
