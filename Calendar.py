from tkinter import *
import calendar


def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()



new = Tk()
new.config(background='grey')
new.title("Calender")
new.geometry("250x140")
cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
cal.grid(row=1, column=1)
year = Label(new, text="Enter year", bg='dark grey')
year.grid(row=2, column=1)
year_field=Entry(new)
year_field.grid(row=3, column=1)
button = Button(new, text='Show Calender',fg='Black',bg='Blue',command=showCalender)
button.grid(row=4, column=1)
button1 = Button(new, text='Exit',fg='Black',bg='Blue',command=new.destroy())
button1.grid(row=6, column=1)
new.mainloop()
