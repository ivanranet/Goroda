from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 3)
            lon = round(results[0]['geometry']['lng'], 3)
            return f'широта {lat}, долгота {lon}'
        else:
            return 'Город не найден.'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates(event = None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text = f'Координаты города {city}:\n {coordinates}')


key = '8d3bbb4150fa4de7b811b9aab057007d'

window = Tk()
window.title('Координаты городов')
window.geometry('350x100')

entry = Entry()
entry.pack()
entry.bind('<Return>',show_coordinates)

button = Button(text = 'Поиск координат', command = show_coordinates)
button.pack()

label = Label(text = 'Введите название города')
label.pack()

window.mainloop()