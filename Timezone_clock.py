from tkinter import*
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry('800x700')
root.configure(bg="white")

usa_img=ImageTk.PhotoImage(Image.open("usa_map.png"))
india_img=ImageTk.PhotoImage(Image.open("India_map.png"))  
australia_img=ImageTk.PhotoImage(Image.open("australia_map.png"))     
japan_img=ImageTk.PhotoImage(Image.open("Japan_map.png"))   

world_time_l=Label(root,text="World Time")
world_time_l.place(relx=0.5,rely=0.01,anchor=CENTER)

Ind_Name_l=Label(root,text="India",bg="white",fg="orange")
Ind_Name_l.place(relx=0.2,rely=0.03,anchor=CENTER)
Ind_clock_img=Label(root,highlightthickness=5,borderwidth=2,relief=SOLID)
Ind_clock_img.place(relx=0.2,rely=0.22,anchor=CENTER)
Ind_clock_img['image']=india_img
Ind_clock_time=Label(root,bg="white")
Ind_clock_time.place(relx=0.2,rely=0.43,anchor=CENTER)

USA_Name_l=Label(root,text="USA",bg="white",fg="orange")
USA_Name_l.place(relx=0.8,rely=0.03,anchor=CENTER)
USA_clock_img=Label(root,highlightthickness=5,borderwidth=2,relief=SOLID)
USA_clock_img.place(relx=0.8,rely=0.22,anchor=CENTER)
USA_clock_img['image']=usa_img
USA_clock_time=Label(root,bg="white")
USA_clock_time.place(relx=0.8,rely=0.43,anchor=CENTER)

Australia_Name_l=Label(root,text="Australia",bg="white",fg="orange")
Australia_Name_l.place(relx=0.2,rely=0.53,anchor=CENTER)
Australia_clock_img=Label(root,highlightthickness=5,borderwidth=2,relief=SOLID)
Australia_clock_img.place(relx=0.2,rely=0.72,anchor=CENTER)
Australia_clock_img['image']=australia_img
Australia_clock_time=Label(root,bg="white")
Australia_clock_time.place(relx=0.2,rely=0.93,anchor=CENTER)

Japan_Name_l=Label(root,text="Japan",bg="white",fg="orange")
Japan_Name_l.place(relx=0.8,rely=0.53,anchor=CENTER)
Japan_clock_img=Label(root,highlightthickness=5,borderwidth=2,relief=SOLID)
Japan_clock_img.place(relx=0.8,rely=0.72,anchor=CENTER)
Japan_clock_img['image']=japan_img
Japan_clock_time=Label(root,bg="white")
Japan_clock_time.place(relx=0.8,rely=0.93,anchor=CENTER)

class India():
    def time(self):
        clock=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(clock)
        current_time=local_time.strftime("%H:%M:%S")
        Ind_clock_time['text']="Time: "+current_time
        Ind_clock_time.after(200,self.time)
        
class USA():
    def time(self):
        clock=pytz.timezone("US/Central")
        local_time=datetime.now(clock)
        current_time=local_time.strftime("%H:%M:%S")
        USA_clock_time['text']="Time: "+current_time
        USA_clock_time.after(200,self.time)
        
class Australia():
    def time(self):
        clock=pytz.timezone("Australia/ACT")
        local_time=datetime.now(clock)
        current_time=local_time.strftime("%H:%M:%S")
        Australia_clock_time['text']="Time: "+current_time
        Australia_clock_time.after(200,self.time)
        
class Japan():
    def time(self):
        clock=pytz.timezone("Asia/Tokyo")
        local_time=datetime.now(clock)
        current_time=local_time.strftime("%H:%M:%S")
        Japan_clock_time['text']="Time: "+current_time
        Japan_clock_time.after(200,self.time)

obj_India=India()
obj_USA=USA()
obj_Australia=Australia()
obj_Japan=Japan()

btn_India=Button(root,text="Show time",bg="white",fg="orange",command=obj_India.time())
btn_India.place(relx=0.2,rely=0.47,anchor=CENTER)

btn_USA=Button(root,text="Show time",bg="white",fg="orange",command=obj_USA.time)
btn_USA.place(relx=0.8,rely=0.47,anchor=CENTER)

btn_australia=Button(root,text="Show time",bg="white",fg="orange",command=obj_Australia.time)
btn_australia.place(relx=0.2,rely=0.97,anchor=CENTER)

btn_japan=Button(root,text="Show time",bg="white",fg="orange",command=obj_Japan.time)
btn_japan.place(relx=0.8,rely=0.97,anchor=CENTER)

root.mainloop()