from opencage.geocoder import OpenCageGeocode


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


key = '...'
city = 'Эквадор'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')