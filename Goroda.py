from auto_py_to_exe.config import language_hint
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return 'Город не найден.'
    except Exception as e:
        return f'Возникла ошибка: {e}'


key = '...'
city = 'London'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')