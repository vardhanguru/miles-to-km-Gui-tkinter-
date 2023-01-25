# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
window=tkinter.Tk()
window.title("rupee to us dollar")
window.minsize(width=300,height=150)


my_label=tkinter.Label(text="0")
my_label.place(x=80,y=40)

texts=tkinter.Label(text="is eual to ")
texts.place(x=20,y=40)

miles=tkinter.Label(text="Dollars")
miles.place(x=20,y=20)
def on_click():
    my_label['text']=str(81.56*int(entry.get()))+' Rupee'
button=tkinter.Button(text="click me",borderwidth=1,command=on_click)
button.place(x=120,y=60)

entry=tkinter.Entry()
entry.place(x=70,y=20)




window.mainloop()
