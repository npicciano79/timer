#gui timer
import tkinter as tk


#def timer():






r=tk.Tk()
r.title("Timer")
r.geometry("420x300")
text_font=("Helvetical", 30,'bold')
background='#add8e6'
s_frame=tk.Frame(r,bg=background)
s_frame.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
t_text=tk.Text(s_frame,height=5, width=25,font=text_font)
t_text.place(relx=0.35,rely=0.1,relwidth=0.3,relheight=0.2)
s_button=tk.Button(s_frame,text="Start",command=lambda:timer(t_text.get))
s_button.place(relx=0.4,rely=0.5,relheight=0.2,relwidth=0.2)


def timer(test):
    print(test)


if __name__=="__main__":
     r.mainloop()
    