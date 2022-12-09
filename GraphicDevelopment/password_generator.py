import tkinter as tk
import secrets
import string

def generate():
    size = int(label_input.get())
    if size > 0:
        spec = "[]{}%#&*\|?/.<>,!()@"
        alphabet = string.ascii_letters + string.digits + spec
        password_str.set(''.join(secrets.choice(alphabet) for i in range(size)))
    else:
        password_str.set("Incorrect length")


window = tk.Tk()

password_str = tk.StringVar(value="Password generator")
password = tk.Label(textvariable=password_str)
simple_text = tk.Label(text="Length")
label_input = tk.Entry()
label_input.insert(0, "10")

btn = tk.Button(text="Generate", command=generate, padx=10)

password.grid(row=0, column=1)
simple_text.grid(row=1, column=0)
label_input.grid(row=1, column=1)
btn.grid(row=1, column=2)


window.mainloop()