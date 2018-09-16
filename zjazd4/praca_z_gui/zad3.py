import tkinter

from zjazd4.praca_z_siecia.zad2_dobry import get_location_id, get_location_weather, present_results

def pobierz_pogode():
    lokalizacja = lokalizacja_entry.get()
    lok_id = get_location_id(lokalizacja)
    pogoda = get_location_weather(lok_id)
    output = present_results(pogoda)
    pogoda_label.configure(text=output)


root = tkinter.Tk()
root.title("Pogoda")

lokalizacja_label = tkinter.Label(master=root, text="Lokalizacja")
lokalizacja_label.pack()

lokalizacja_entry = tkinter.Entry(master=root)
lokalizacja_entry.pack()

pobierz = tkinter.Button(master=root, text="Sprawdź", command=pobierz_pogode)
pobierz.pack()
pogoda_label = tkinter.Label(master=root, text=" - ")
pogoda_label.pack()


root.mainloop()