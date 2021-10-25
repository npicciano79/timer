import tkinter as tk

#create tk instance 
r=tk.Tk()
r.geometry("400x400")
r.title("Timer")
text_font=("Helvetical", 30,'bold')
background='#add8e6'
background2='#000000'

#create 2 frames
start_frame=tk.Frame(r,bg=background)
time_frame=tk.Frame(r,bg=background2)


#button to enter time and switch frames
#on start frame, records time, calls timer frame
s_button=tk.Button(start_frame,text="Start",command=lambda:timer())             
s_button.place(relx=0.4,rely=0.7,relheight=0.2,relwidth=0.2)

#on timer frame, stops timer, calls start frame
t_button=tk.Button(time_frame,text="Stop",command=lambda:start())             
t_button.place(relx=0.4,rely=0.7,relheight=0.2,relwidth=0.2)


def timer():
    time_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.5)
    start_frame.place_forget()


def start():
    start_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
    time_frame.place_forget()



if __name__=="__main__":
    start()
    r.mainloop()



