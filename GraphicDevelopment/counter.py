import tkinter as tk
CNT_MAX = 10

window = tk.Tk()

def increment():
    val = int(val_cnt.get())
    val_cnt.set(val + 1)
    if val >= CNT_MAX:
        cnt.configure(bg="red")


def decrement():
    val = int(val_cnt.get())
    if val > 0:
        val_cnt.set(val - 1)
    if val <= CNT_MAX:
        cnt.configure(bg="green")

val_cnt = tk.StringVar(value='0')
cnt = tk.Label(textvariable=val_cnt, padx=50, pady=10, bg="green")
btn_incr = tk.Button(command=increment, text='+', padx=20, pady=10)
btn_decr = tk.Button(command=decrement, text='-', padx=20, pady=10)

btn_decr.grid(row=0, column=0)
cnt.grid(row=0, column=1)
btn_incr.grid(row=0, column=2)

window.mainloop()