from tkinter import *

window = Tk()
window.title("Převod měn z CZK na EUR")
window.minsize(200,100)
window.resizable(False,False)
window.config(bg="#061856")
window.iconbitmap("C:/Users/Badsoul/PycharmProjects/test/icon.ico")
def count_currency():
    amount_eur =float(amount_input.get()) / 24.40
    result_label["text"] = round(amount_eur,2)

#1eur = 24,40
# Vstup od uživatele
amount_input = Entry(width=10,font=("Helvetica",15))
amount_input.grid(row=0,column=0, padx= 10,pady=10)
#label_CZK
label_1=Label(text="CZK",font=("Helvetica",15), bg="#061856", fg="white")
label_1.grid(row=0,column=1)
#result_label
result_label = Label(text="0",font=("Helvetica",15),bg="#061856", fg="white")
result_label.grid(row=1,column=0)
#label_EUR
label_eur= Label(text="EUR",font=("Helvetica",15),bg="#061856", fg="white")
label_eur.grid(row=1,column=1)

#tlačítko
count_button= Button(text="Přepočítat",font=("Helvetica",15), command=count_currency)
count_button.grid(row=0,column=2, padx=10,pady=10)


#hlavní cyklus
window.mainloop()