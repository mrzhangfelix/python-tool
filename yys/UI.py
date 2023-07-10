import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
style = Style()
window.title("yyds")

# 功能1
frame1 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame1.grid(row=0, column=0)
label = tk.Label(master=frame1, text="文本标签")
entry = tk.Entry(master=frame1, width=20)
btn = tk.Button(master=frame1, text="Click me!", width=20)

label.pack(side=tk.LEFT)
entry.pack(side=tk.LEFT)
btn.pack(side=tk.LEFT)

# 功能2
frame2 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame2.grid(row=1, column=0)

label2 = tk.Label(master=frame2, text="文本标签")
entry2 = tk.Entry(master=frame2, width=20)
btn2 = tk.Button(master=frame2, text="Click me!", width=20)

label2.pack(side=tk.LEFT)
entry2.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)

window.mainloop()
