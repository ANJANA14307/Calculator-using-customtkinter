import customtkinter as ctk

#create a window set geometry and size
root=ctk.CTk()
root.geometry("1200x1200")
root.title("Simple Calculator")

def calculate(op):
    n1=float(e1.get())
    n2=float(e2.get())
    if op=='+':
        res.configure(root,text=f"Sum :{n1+n2}")
    elif op=='-':
        res.configure(root,text=f"Differnece :{n1-n2}")
    elif op=='*':
        res.configure(root,text=f"Product :{n1*n2}")
    elif op=='/':
        res.configure(root,text=f"Division :{n1/n2}")

        
    
    
def add():
    calculate('+')
  
def sub():
    calculate('-')
   
def mul():
    calculate('*')
   
def div():
    calculate('/')
   

#create entry feilds 

e1=ctk.CTkEntry(root,placeholder_text="Number_1")
e1.pack(pady=10)

e2=ctk.CTkEntry(root,placeholder_text="Numbert_2")
e2.pack(pady=10)

#create label
res=ctk.CTkLabel(root,text="RESULT")
res.pack(pady=10)



b1=ctk.CTkButton(root,text="Click to add",command=add)
b1.pack(pady=10)

b2=ctk.CTkButton(root,text="Click to Subract",command=sub)
b2.pack(pady=10)

b3=ctk.CTkButton(root,text="Click to Multiply",command=mul)
b3.pack(pady=10)

b4=ctk.CTkButton(root,text="Click to Divide",command=div)
b4.pack(pady=10)

root.mainloop()

    


