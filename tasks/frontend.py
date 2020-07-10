"""
program to save tasks 
i need to have [tasknum, time, date, description]

user can:
viwe all tasks
search for task
add task
update task
delete task
close
"""
from tkinter import *

window=Tk()
#labels

l1=Label(window,text="task")
l1.grid(row=0, column=0)

l2=Label(window,text="description")
l2.grid(row=0, column=2)

l3=Label(window, text="date")
l3.grid(row=1, column=0)

l4=Label(window, text="time")
l4.grid(row=1, column= 2)

# text space

task_text=StringVar()
e1=Entry(window,textvariable=task_text)
e1.grid(row=0, column=1)

desc_text=StringVar()
e2=Entry(window,textvariable=desc_text)
e2.grid(row=0, column=3)

date_text=StringVar()
e3=Entry(window,textvariable=date_text)
e3.grid(row=1, column=1)

time_text=StringVar()
e4=Entry(window,textvariable=time_text)
e4.grid(row=1, column=3)

#list box for the tasks
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scroll
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# configure for scroll and list box
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Button
b1=Button(window,text="View all", width=12)
b1.grid(row=2,column=3)

b1=Button(window,text="Search Task", width=12)
b1.grid(row=3,column=3)

b1=Button(window,text="Add Task", width=12)
b1.grid(row=4,column=3)

b1=Button(window,text="Update Task", width=12)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete Task", width=12)
b1.grid(row=6,column=3)

b1=Button(window,text="Close", width=12)
b1.grid(row=7,column=3)





window.mainloop()