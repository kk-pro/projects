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
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(task_text.get(),date_text.get(),time_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(task_text.get(),desc_text.get(),date_text.get(),time_text.get())
    list1.delete(0,END)
    list1.insert(0,(task_text.get(),desc_text.get(),date_text.get(),time_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],task_text.get(),desc_text.get(),date_text.get(),time_text.get())


window=Tk()
#window title

window.wm_title("Task manger")
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

#binding list with selecte method
list1.bind('<<ListboxSelect>>',get_selected_row)

#Button
b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b1=Button(window,text="Search Task", width=12,command=search_command)
b1.grid(row=3,column=3)

b1=Button(window,text="Add Task", width=12,command=add_command)
b1.grid(row=4,column=3)

b1=Button(window,text="Update Task", width=12,command=update_command)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete Task", width=12,command=delete_command)
b1.grid(row=6,column=3)

b1=Button(window,text="Close", width=12,command=window.destroy)
b1.grid(row=7,column=3)





window.mainloop()