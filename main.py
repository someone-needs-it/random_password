import tkinter

window = tkinter.Tk()
window.geometry("1920x1080")
window.title("Генерация пароля бля")
window.config(background="blue")
number_of_simbol = 10
def password(number_of_simbol=6):
    import random
    simbols = []
    for i in range(number_of_simbol):
        num = random.randint(1,3)
        if num == 1:
            simbols.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
        elif num == 2:
            simbols.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        elif num == 3:
            simbols.append(random.choice("0123456789"))
    password1 = "".join(str(simb) for simb in simbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password1)
text = tkinter.Text(
    font=("arial", 20, "bold"),
    height=1,
    width=number_of_simbol+1,
    bg="black",
    fg="white",
    borderwidth=15
)
text.pack(expand=1)
tkinter.Button(
    text="Generate",
    font=("arial", 20, "bold"),
    bg="white",
    fg="black",
    borderwidth=0,
    command=lambda: password(number_of_simbol)
).pack(expand=1)



window.mainloop()










































































































































































































































