from tkinter.ttk import *
from tkinter import *
import pyshorteners

def shorten():
    url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    output.config(state='normal')
    output.delete('1.0', 'end')
    output.insert('end', short_url)
    output.config(state='disabled')

bg_color='#FFFFFF'
col='#282828'
col1='#8B8B65'
root = Tk()
root.title("URL Shortener")
root.geometry('450x200')
root.configure(bg=col1)
root.resizable(width=FALSE, height=FALSE)

label = Label(root, text="ENTER URL", font=('Arial 14 bold'),bg=col1)
label.pack()
label.place(x=165,y=4)

entry = Entry(root,width=250)
entry.pack()
entry.place(x=0,y=40)

button = Button(root, text="SHORTEN", command=shorten, font=('arial 12 bold'), bg='#FFFFFF')
button.pack()
button.place(x=170,y=70)

output_label = Label(root, text="SHORTENED URL", font=('Arial 14 bold'),bg=col1)
output_label.pack()
output_label.place(x=140,y=115)

output = Text(root, height=1, state='disabled')
output.pack()
output.place(x=0,y=150)

root.mainloop()