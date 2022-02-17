from tkinter import *
root = Tk()
root.geometry("330x280")

def getvals():
    print("Aceito")

# Cabeçalho
Label(root, text="Cadastro em Python", font="ar 15 bold").grid(row=0, column=3)

# Campo de dados
name = Label(root, text="Nome")
phone = Label(root, text="Fone")
gender = Label(root, text="Gênero")
emergency = Label(root, text="Emergência")
paymentmood = Label(root, text="Pagamento")

# Ajustando a entrada de dados
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variáveis para armazenar os dados inseridos
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Criando os campos de entrada de dados
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)

# Ajustando os campos de entrada
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Criando uma Checkbox
checkbtn = Checkbutton(text="Lembrar de mim", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

# Botão de Confirmar
Button(text="Mandar", command=getvals).grid(row=7, column=3)

root.mainloop()