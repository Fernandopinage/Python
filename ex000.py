from tkinter import *


painel = Tk()

painel.title("Primeiro programa")
painel.geometry("500x300")
login = Label(painel,text ="Login:").grid(row=0,column =0)
Password = Label(painel, text = "Password:").grid(row =1 , column = 0)

print("olá mundo")
painel.mainloop()


