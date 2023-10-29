# Εφαρμογή Επίβλεψης Ανανεώσιμων Πηγών Ενέργειας για την Ελλάδα

Αυτή είναι μια απλή εφαρμογή που χρησιμοποιεί το API του [data.gov.gr](https://data.gov.gr/) για να παρέχει πληροφορίες σχετικά με την ενέργεια που παράγεται από ανανεώσιμες πηγές ενέργειας.

## Περιγραφή

Η εφαρμογή σας επιτρέπει να επιλέξετε μια περίοδο (από - έως) και να ανακτήσετε πληροφορίες για την παραγωγή ενέργειας από ανανεώσιμες πηγές για αυτήν την περίοδο. Η εφαρμογή εμφανίζει επίσης τη συνολική ενέργεια που παράχθηκε κατά τη διάρκεια της επιλεγείσας περιόδου και δημιουργεί ένα γράφημα με την εξέλιξη της παραγωγής.

## Απαιτήσεις

Πριν χρησιμοποιήσετε την εφαρμογή, πρέπει να εγκαταστήσετε τα ακόλουθα πακέτα:

- [Python](https://www.python.org/) (το πρόγραμμα έχει αναπτυχθεί με Python 3)
- [Βιβλιοθήκη tkinter](https://docs.python.org/3/library/tkinter.html)
- [Βιβλιοθήκη pydatagovgr](https://pypi.org/project/pydatagovgr/)
- [Βιβλιοθήκη matplotlib](https://matplotlib.org/)

Μπορείτε να εγκαταστήσετε τις παραπάνω βιβλιοθήκες χρησιμοποιώντας το pip:

``` pip install tk ```
``` pip install pydatagovgr ```
``` pip install matplotlib ```

## Χρήση

1. Εκτελέστε το αρχείο `main.py` για να ανοίξετε την εφαρμογή.
2. Επιλέξτε την περίοδο από - έως χρησιμοποιώντας τα αντίστοιχα dropdown μενού.
3. Πατήστε το κουμπί "Load Data" για να ανακτήσετε τα δεδομένα και να εμφανίσετε το γράφημα και την συνολική ενέργεια.

# Greece Renewable Resources Monitoring Application

This is a simple application that utilizes the [Public Information of Greece API](https://data.gov.gr/) to provide information about energy generated from renewable sources in Greece.

## Description

The application allows you to select a time period (from - to) and retrieve information about energy production from renewable sources for that period. The application also displays the total energy produced during the selected period and creates a chart showing the evolution of production.

## Requirements

Before using the application, you need to install the following packages:

- [Python](https://www.python.org/) (the program is developed using Python 3)
- [tkinter library](https://docs.python.org/3/library/tkinter.html)
- [pydatagovgr library](https://pypi.org/project/pydatagovgr/)
- [matplotlib library](https://matplotlib.org/)

You can install these libraries using pip:

``` pip install tk ```
``` pip install pydatagovgr ```
``` pip install matplotlib ```

## Usage

1. Run the `main.py` file to open the application.
2. Select the time period (from - to) using the corresponding dropdown menus.
3. Click the "Load Data" button to retrieve the data and display the chart and total energy.

