import tkinter as tk

class generateConfigFile(self):
    print('wassup')
    tk.Label(self, text="First Name").grid(row=0)
    tk.Label(self, text="Last Name").grid(row=1)

    e1 = tk.Entry(self)
    e2 = tk.Entry(self)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)