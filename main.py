import tkinter
from tkinter import *

def bmi_calculate():
    weight=my_wentry.get()
    height=my_hentry.get()

    if weight == "" or height == "" :
        last_lable.config(text="make sure you enter your kg and cm ")

    else:
        try:
            bmi= float(weight)/ (float(height)/100) ** 2
            print(bmi)
            last_lable.config(text=f"your bmi is {round(bmi,1)}")
            print(last_lable)
            if bmi<18.5:
                last_lable.config(text=f"your bmi is {round(bmi, 1)}  Thinness")
            if 18.6 < bmi <25:
               last_lable.config(text=f"your bmi is {round(bmi, 1)}  normal")
            if bmi>25:
                last_lable.config(text=f"your bmi is {round(bmi, 1)}  Overweight")



        except:
            last_lable.config(text="write number only!!")




screan= Tk()
screan.minsize(width=450, height=300)
screan.config(bg="#3390FF")
my_wlabel=tkinter.Label(text="enter your weight (in kg)", font=("arial", 12, "italic"))
my_wlabel.pack()
my_wentry= tkinter.Entry()
my_wentry.pack(pady=10)
my_wlabel.config(bg="#3390FF")



a = "enter your height (in cm)"
my_hlabel=tkinter.Label(text=a,font=("arial", 12, "italic"))
my_hlabel.pack(pady=10)
my_hlabel.config(bg="#3390FF")


my_hentry=tkinter.Entry()
my_hentry.pack(pady=10)



my_button=tkinter.Button(text="calculate", command=bmi_calculate )
my_button.pack()

last_lable=tkinter.Label(font=("arial", 15, "italic"))

last_lable.pack(pady=5)
last_lable.config(bg="#3390FF" )
screan.mainloop()









