import sys

import tkinter as tk
#addition
def add():
        try:
            
         num1=int(entry1.get())
         num2=int(entry2.get())
         result = num1 + num2
         #addition
         result_label.config(text=f"Result={result}")
         #sub
         
        except ValueError:
         result_label.config(text=f"You not enter a number !")
#substraction        
def sub():
    try:
        num1 = int(entry1.get()) 
        num2= int(entry2.get())
        result = num1 - num2  
        result_label.config(text=f"Result={result}")         
    except ValueError:
         result_label.config(text=f"You not enter a number !")

#multiplication
def mul():
    try:
        num1 = int(entry1.get()) 
        num2= int(entry2.get())
        result = num1 * num2  
        result_label.config(text=f"Result={result}")         
    except ValueError:
         result_label.config(text=f"You not enter a number !")
#divition
def div():
    try:
        num1 = int(entry1.get()) 
        num2= int(entry2.get())
        result = num1 / num2  
        result_label.config(text=f"Result={result}")         
    except ValueError:
         result_label.config(text=f"You not enter a number !")






def main():
    global entry1,entry2,result_label,root,add_button,sub_button,mul_button,button
    root=tk.Tk()
    root.title("simple calculator")
    root.geometry("300x200")

    label = tk.Label(root,text="*Hello I am calculator*")
    label.pack(pady=20)
     
     #for input 1st number 
    label1=tk.Label(root,text="Enter a 1st number:")
    label1.pack(pady=10)
    entry1=tk.Entry(root,width=20)
    entry1.pack(pady=5)

    #for input 2st number 
    label2=tk.Label(root,text="Enter a 2nd number:")
    label2.pack(pady=10)

    entry2=tk.Entry(root,width=20)
    entry2.pack(pady=5)
#result of addition
    result_label=tk.Label(root,text=" ",fg="red")
    result_label.pack(pady=10)

    
    add_button=tk.Button(root, text="Addition",command=add)
    add_button.pack(pady=10)
    sub_button=tk.Button(root,text="Substraction",command=sub)
    sub_button.pack(pady=10)
    mul_button=tk.Button(root,text="Multiplication",command=mul)
    mul_button.pack(pady=10)
    div_button=tk.Button(root,text="Divition",command=div)
    div_button.pack(pady=20)

    root.mainloop()
    sys.exit()

main()
