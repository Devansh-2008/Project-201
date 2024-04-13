from tkinter import *
window = Tk()

def Calculate_Interest():
    global result_label
    p = float(principle_entry.get())
    r = float(interest_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    result_label.destroy()
    result_label=Label(result_frame,text=interest, bg = "lightgreen", font=("Calibri", 12), width=33)
    result_label.place(x=20,y=40)
    result_label.pack()



window.title('Simple Interest Calculator')
window.geometry("400x400")
window.configure(bg = 'lightgreen')

head_label = Label(window,text = "Simple Interest Calculator",fg = "black",bg = "lightgreen",font = ("Calibri",12),bd = 5)
head_label.place(x = 50,y = 20)

principle_label = Label(window, text = "Principle : ",fg = "black",bg = "lightgreen",font = ("Calibri",12),bd = 1)
principle_label.place(x = 20,y = 90)

principle_entry = Entry(window,text = "",bd = 2,width = 22)
principle_entry.place(x = 150,y = 90)

interest_label = Label(window, text = "Rate of interest : ",fg = "black",bg = "lightgreen",font = ("Calibri",12),bd = 1)
interest_label.place(x = 20,y = 140)

interest_entry = Entry(window,text = "",bd = 2,width = 22)
interest_entry.place(x = 150,y = 140)

time_label = Label(window, text = "Time period : ",fg = "black",bg = "lightgreen",font = ("Calibri",12),bd = 1)
time_label.place(x = 20,y = 190)

time_entry = Entry(window,text = "",bd = 2,width = 22)
time_entry.place(x = 150,y = 190)

calc_button = Button(window,text = "Calculate",fg = "black",bg = "green",width = 20,bd = 4,command = Calculate_Interest)
calc_button.place(x = 90,y = 250)

result_frame = LabelFrame(window,text = "Result",bg = "lightgreen",font = ("Calibri",12))
result_frame.pack(padx = 20,pady = 20)
result_frame.place(x = 20,y = 300)

result_label=Label(result_frame,text=" ", bg = "lightgreen", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()