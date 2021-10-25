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
t_text=tk.Text(s_frame,height=5, width=25)
t_text.pack()

#s_button=tk.Button(r,text="Start", command=lambda:timer())



if __name__=="__main__":
     r.mainloop()
    