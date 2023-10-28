import tkinter as tk
from pydatagovgr import DataGovClient
from tkinter import *

#τα του API κτλπ
gov = DataGovClient(token='39cfd83f0388cc86536960a2eebc748761d1accc')
energy_data = gov.query('admie_realtimescadares', date_from='2023-10-25', date_to='2023-10-27')

mwh = []
count = len(energy_data) - 1

while count >= 0:
    entry = {
        'date': energy_data[count]['date'].split('T')[0],
        'energy_mwh': energy_data[count]['energy_mwh']
    }
    mwh.append(entry)
    count -= 1


#for entry in mwh:
#    if entry['date'] == target:
#        print(entry)

window = tk.Tk()
window.title("Greece Renewable Resources")
window.geometry("600x600") 


canvas = tk.Canvas(window, width=570, height=570)
canvas.pack()

canvas.create_text(285, 125, text="Sumbit Date", font=("Helvetica", 24))

#εκχωρηση ημερομηνιας 

#Day#
label = tk.Label(window, text="Επιλέξτε ένα έτος:")
label.pack(pady=10)

# Λίστα με τα έτη
days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

# StringVar για να αποθηκεύσετε την επιλογή
selected_option = tk.StringVar()

# Dropdown Menu
dropdown1 = tk.OptionMenu(window, selected_option, *days)
dropdown1.pack()


#Month#
label = tk.Label(window, text="Επιλέξτε ένα έτος:")
label.pack(pady=10)

# Λίστα με τα έτη
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

# StringVar για να αποθηκεύσετε την επιλογή
selected_option = tk.StringVar()

# Dropdown Menu
dropdown2 = tk.OptionMenu(window, selected_option, *months)
dropdown2.pack()


#Year#
label = tk.Label(window, text="Επιλέξτε ένα έτος:")
label.pack(pady=10)

# Λίστα με τα έτη
years = ["2023", "2022", "2021", "2020"]

# StringVar για να αποθηκεύσετε την επιλογή
selected_option = tk.StringVar()

# Dropdown Menu
dropdown3 = tk.OptionMenu(window, selected_option, *years)
dropdown3.pack()




button = Button(window, text="Load Data")
button.pack()
button.place(x=235, y=180)

window.mainloop()