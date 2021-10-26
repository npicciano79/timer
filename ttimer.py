import tkinter as tk
from typing import Text

#create tk instance 
r=tk.Tk()
r.geometry("400x400")
r.title("Timer")
text_font=("Helvetical", 30,'bold')
background='#add8e6'
background2='#000000'

#create 2 frames
start_frame=tk.Frame(r,bg=background)
time_frame=tk.Frame(r,bg=background)


#button to enter time and switch frames
#on start frame, records time, calls timer frame
s_button=tk.Button(start_frame,text="Start",command=lambda:timer())             
s_button.place(relx=0.4,rely=0.7,relheight=0.2,relwidth=0.2)

#on timer frame, stops timer, calls start frame
t_button=tk.Button(time_frame,text="Stop",command=lambda:start())             
t_button.place(relx=0.4,rely=0.7,relheight=0.2,relwidth=0.2)

#user enters time in textbox
s_text=tk.Text(start_frame,height=5, width=25,font=text_font)
s_text.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.2)

#directions label
s_title=tk.Label(start_frame,text="Enter your time and press Start",bg=background)
s_title.place(relx=0.25,rely=0.5,relwidth=0.5,relheight=0.2)




#timer frame
def timer():
    inputVal=int(s_text.get("1.0","end-1c"))
    #print(inputVal)
    time_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
    start_frame.place_forget()
    #countdown label found on timer frame
    countdown=tk.Label(time_frame,text=inputVal)
    countdown.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.2)
    countdown(inputVal,countdown)
 
#starting frame
def start(): 
    start_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
    time_frame.place_forget()



#countdown timer
def countdown(inputVal,countdown):
    print(inputVal)
    #timer countdown, appear on time_frame, called by timer
    if inputVal > 0:
        inputVal-=1
        countdown.set(inputVal)
        r.after(1000,lambda:countdown(inputVal,countdown))
    else:
        close()


if __name__=="__main__":
    start()
    r.mainloop()



