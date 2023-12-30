from tkinter import *

class Cifra(Tk):
    def __init__(self):
        super().__init__()
        self.title("Cifra")

        self.f0 = Frame(self)
        self.f0.grid(row=0, column=0, padx=50, pady=10)
        self.titulo = Label(self.f0, text='Cifra de César', font=['Times New Roman', '25', 'bold'])
        self.titulo.grid(row=0, column=0)
        
        self.f1 = Frame(self)
        self.f1.grid(row=1, column=0, padx=50, pady=10)

        self.l1 = Label(self.f1, text='Texto')
        self.l1.grid(row=0, column=0)

        self.palavra = Entry(self.f1)
        self.palavra.grid(row=1, column=0)

        self.l2 = Label(self.f1, text='Chave')
        self.l2.grid(row=0, column=1)

        self.chave = Entry(self.f1)
        self.chave.grid(row=1, column=1)

        self.f2 = Frame(self)
        self.f2.grid(row=2, column=0, padx=50, pady=10)

        self.cifrarbttn = Button(self.f2, text='Cifrar', command=self.cifrar)
        self.cifrarbttn.grid(row=0, column=0)

        self.decifrarbttn = Button(self.f2, text='Decifrar', command=self.decifrar)
        self.decifrarbttn.grid(row=0, column=1)

        self.f3 = Frame(self)
        self.f3.grid(row=3, column=0, padx=50, pady=10)

        self.msg = Label(self.f3, text='')
        self.msg.grid(row=0, column=0)

        self.mainloop()

    def cifrar(self):
        from ciframe import ciframe
        try:
            p = self.palavra.get()
            chave_k = int(self.chave.get())
            self.msg.config(text=ciframe(p, chave_k))
        except (ValueError, UnboundLocalError):
            from tkinter import messagebox
            messagebox.showerror("Erro", 'Os valores colocados estão incorretos.')

    def decifrar(self):
        from deciframe import deciframe
        try:
            p = self.palavra.get()
            chave_k = int(self.chave.get())
            self.msg.config(text=deciframe(p, chave_k))
        except (ValueError, UnboundLocalError):
            from tkinter import messagebox
            messagebox.showerror("Erro", 'Os valores colocados estão incorretos.')

if __name__ == '__main__':
    Cifra()