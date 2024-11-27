from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 3)
            lon = round(results[0]['geometry']['lng'], 3)
            country = results[0]['components']['country']
            money = results[0]['annotations']['currency']['name']
            osm_url = f'https://www.openstreetmap.org/?mlat={lat}&mlon={lon}'

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']

                return {
                    'coordinates': f'широта {lat},\nдолгота {lon},\nстрана: {country},\nрегион: {region},\nвалюта: {money}',
                    'map_url': osm_url
                        }
            else:
                return {
                    'coordinates': f'широта {lat},\nдолгота {lon},\nстрана: {country},\nвалюта: {money}',
                    'map_url': osm_url
                        }
        else:
            return 'Город не найден.'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates(event = None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text = f'Координаты города {city}:\n {result['coordinates']}')
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


def clear_entry():
    entry.delete(0, END)


key = '...'
map_url = ''

window = Tk()
window.title('Координаты городов')
window.geometry('350x210')

entry = Entry()
entry.pack()
entry.bind('<Return>',show_coordinates)

button = Button(text = 'Поиск координат', command = show_coordinates)
button.pack()

label = Label(text = 'Введите название города')
label.pack()

map_button = Button(text = 'Показать карту', command = show_map)
map_button.pack()

clear_button = Button(text = 'Очистить', command = clear_entry)
clear_button.pack()

window.mainloop()
