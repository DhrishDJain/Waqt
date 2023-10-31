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

def time1(e):
        global hr
        global enter

        # try:
        #      hr.destroy()
        # except:
        #        pass
        l=Label(enter,font=ds,background="#616161",foreground="#ff7f27")
        l.pack()
    
        def time():
                String = strftime('%I:%M:%S %p')
                l.config(text = String)
                print("x")
                l.after(1000,time)
        time()


def timer2(e):
    global hr
    global l
    # l.config(text="")
    # l.update()

    # enter.update()


    def only_numbers(char):
        if char.isdigit() or char==" ":
            return True
        else:
            return False
    global count
    count=0
    def t(e):
        global count
        temp=list(hr.get())
        if count==1:
            temp.remove(":")
            count=0
        for i in range(len(temp)):
            if temp[i]==":":
                hr.icursor(i+2)
                count+=1
                break


       
        
    validation = root.register(only_numbers)
    hr=tk.Entry(enter) 
    hr.insert(10,"    ")
    hr.insert(20,":")
    hr.insert(10,"    ")
    hr.insert(50,":")
    hr.icursor(8)
    hr.config(font=ds,width=13,border=0,background="#616161",foreground="#ff7f27",validate="key", validatecommand=(validation,"%S"))
    hr.pack(side=LEFT,pady=22)
    root.bind("<Return>",t)

 
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
# if m>60:
#     m=int(input("Plz enter min value in the range of 0 to 60 :"))
# if s>60:
#     s=int(input("Plz enter second value in the range of 0 to 60 :"))

# #main function
# def counter(h,m,s):
#     hs=h*3600
#     ms=m*60
#     ts=hs+ms+s#total no. of seconds
#     while True:
#         print(f" COUNTDOWN {h}:{m}:{s} ",end="\r")
#         time.sleep(1)
#         #various cases to handle hr min and second
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
