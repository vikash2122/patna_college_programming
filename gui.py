import tkinter as tk
def add():
    res=int(entry.get())+int(entry2.get())
    print(res)
    label_text.set(res)

root=tk.Tk()
root.geometry("1080x1080")
label_text=tk.StringVar()
f=tk.Label(text="add two nos",textvariable=label_text,height=2,width=1080)
f.pack()
my_button=tk.Button(root,text="ADD",height=1,width=35,command=add)
my_button.pack()
entry=tk.Entry(root,text="enter a number")
entry.pack(padx=50,pady=50)
entry2=tk.Entry(root)
entry2.pack(pady=60,padx=50)
root.mainloop()
