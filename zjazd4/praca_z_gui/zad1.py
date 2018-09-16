import tkinter

def koszt_spalania():
   spalanie = float(spalanie_entry.get())
   dystans = float(dystans_entry.get())
   cena_paliwo =float(cana_paliwo_entry.get())
   wynik_label.configure(text=f"Koszt przejazdu: {((dystans*spalanie)/100)*cena_paliwo}")

def czysc():
   print(locals())
   print(globals())
   wynik_label.configure(text="Koszt przejazdu: - ")

root = tkinter.Tk()
root.columnconfigure(1, weight=1)
root.title("Koszt przejazdu")

spalanie_label = tkinter.Label(master=root, text="spalanie")
spalanie_label.grid(row=0, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=0, column=1)


dystans_label = tkinter.Label(master=root, text="dystans")
dystans_label.grid(row=1, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=1, column=1)


cena_label = tkinter.Label(master=root, text="cena paliwo")
cena_label.grid(row=2, column=0)
cana_paliwo_entry = tkinter.Entry(master=root)
cana_paliwo_entry.grid(row=2, column=1)


koszt_button = tkinter.Button(master=root, text="Koszt", command=koszt_spalania)
koszt_button.grid(row=3, column=1)


czysc_button = tkinter.Button(master=root, text="Czyść", command=czysc)
czysc_button.grid(row=3, column=0)

wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.grid(row=4, column=1)

root.mainloop()




