import tkinter as tk
from pydatagovgr import DataGovClient
from tkinter import *
import matplotlib.pyplot as plt

#τα του API κτλπ
gov = DataGovClient(token='39cfd83f0388cc86536960a2eebc748761d1accc')

window = tk.Tk()
window.title("Greece Renewable Resources")
window.geometry("600x600")
window.maxsize(width=600, height=600)


canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

canvas.create_text(50, 50, text="From:", font=("Helvetica", 24))
canvas.create_text(250, 50, text="To:", font=("Helvetica", 24))

def get_data(from_data, to_data):
    energy_data = gov.query('admie_realtimescadares', date_from=from_data, date_to=to_data)
    global mwh
    mwh = []
    count = len(energy_data) - 1

    while count >= 0:
        entry = {
            'date': energy_data[count]['date'].split('T')[0],
            'energy_mwh': energy_data[count]['energy_mwh']
        }
        mwh.append(entry)
        count -= 1

    print(entry)
    

def get_date():
    from_year = int(selected_year_from.get())
    from_month = int(selected_month_from.get())
    from_day = int(selected_day_from.get())

    to_year = int(selected_year_to.get())
    to_month = int(selected_month_to.get())
    to_day = int(selected_day_to.get())

    from_year2 = selected_year_from.get()
    from_month2 = selected_month_from.get()
    from_day2 = selected_day_from.get()

    to_year2 = selected_year_to.get()
    to_month2 = selected_month_to.get()
    to_day2 = selected_day_to.get()

    from_date = from_year * 10000 + from_month * 100 + from_day
    to_date = to_year * 10000 + to_month * 100 + to_day

    from_data = from_year2 + '-' + from_month2 + '-' + from_day2
    to_data = to_year2 + '-' + to_month2 + '-' + to_day2


    if from_date < to_date:
        get_data(from_data, to_data)
        total_mwh()
        graph()
    elif from_date == to_date:
        get_data(from_data, to_data)
        total_mwh()
        graph()
    else:
        canvas.create_text(300, 180, text="Error: 'From' date is after 'To' date.", font=("Helvetica", 24), tags="total", fill="red")

def total_mwh():

    total_energy = 0
    
    for entry in mwh:
        total_energy += entry['energy_mwh']   
        
    
    canvas.delete("total")
    canvas.create_text(200, 200, text="Total MWH: " + str(total_energy), font=("Helvetica", 24), tags="total")

def graph():
    if 'mwh' not in globals():
        return  # Δεν υπάρχουν δεδομένα για τη δημιουργία γραφήματος

    dates = [entry['date'] for entry in mwh]
    energy_mwh = [entry['energy_mwh'] for entry in mwh]

    plt.figure(figsize=(12, 6))
    plt.bar(dates, energy_mwh, color='b')
    plt.title('Διακύμανση της τιμής energy_mwh')
    plt.xlabel('Ημερομηνία')
    plt.ylabel('Energy (MWh)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


#εκχωρηση ημερομηνιας 
#from
# Day
day_label = tk.Label(window, text="Ημέρα:")
day_label.pack()
day_label.place(x=20, y=90)

days = [str(i).zfill(2) for i in range(1, 32)]
selected_day_from= tk.StringVar()
dropdown1 = tk.OptionMenu(window, selected_day_from, *days)
dropdown1.pack()
dropdown1.place(x=20, y=110)

# Month
month_label = tk.Label(window, text="Μήνας:")
month_label.pack()
month_label.place(x=75, y=90)

months = [str(i).zfill(2) for i in range(1, 13)]
selected_month_from = tk.StringVar()
dropdown2 = tk.OptionMenu(window, selected_month_from, *months)
dropdown2.pack()
dropdown2.place(x=75, y=110)

# Year
year_label = tk.Label(window, text="Έτος:")
year_label.pack()
year_label.place(x=130, y=90)

years = [str(i) for i in range(2023, 2019, -1)]
selected_year_from = tk.StringVar()
dropdown3 = tk.OptionMenu(window, selected_year_from, *years)
dropdown3.pack()
dropdown3.place(x=130, y=110)


#to
# Day
day_label = tk.Label(window, text="Ημέρα:")
day_label.pack()
day_label.place(x=240, y=90)

days = [str(i).zfill(2) for i in range(1, 32)]
selected_day_to = tk.StringVar()
dropdown1 = tk.OptionMenu(window, selected_day_to, *days)
dropdown1.pack()
dropdown1.place(x=240, y=110)

# Month
month_label = tk.Label(window, text="Μήνας:")
month_label.pack()
month_label.place(x=295, y=90)

months = [str(i).zfill(2) for i in range(1, 13)]
selected_month_to = tk.StringVar()
dropdown2 = tk.OptionMenu(window, selected_month_to, *months)
dropdown2.pack()
dropdown2.place(x=295, y=110)

# Year
year_label = tk.Label(window, text="Έτος:")
year_label.pack()
year_label.place(x=350, y=90)

years = [str(i) for i in range(2023, 2019, -1)]
selected_year_to = tk.StringVar()
dropdown3 = tk.OptionMenu(window, selected_year_to, *years)
dropdown3.pack()
dropdown3.place(x=350, y=110)


button = Button(window, text="Load Data", command=get_date)
button.pack()
button.place(x=450, y=110)

window.mainloop()