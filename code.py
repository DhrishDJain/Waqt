from tkinter import * 
import tkinter as tk

import time

class ui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        self.title('CLOCK')
        self.iconphoto(False,tk.PhotoImage(file="icon3.png"))
        self.maxsize(width=500,height=200)
        self.config(background="#616161")
    



# if __name__=="__main__":
root=ui()
option=Frame(root,background="#616161",border=6)
option.pack(side=LEFT,fill=Y)
im=PhotoImage(file="timericon.png")
im2=PhotoImage(file="timeicon.png")
z=Button(option,image=im2,width=56,height=56,border=0,bg="black",activebackground="#616161")
z.pack(side=TOP,)
z=Button(option,image=im,width=53,height=57,border=0,background="#616161",activebackground="#616161")
z.pack(side=TOP,pady=7)
        
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
