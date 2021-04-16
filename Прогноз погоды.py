import pyowm

owm = pyowm.OWM('222fd6e9f356fdc8a540ddcac8a3b4cb', language = "ru") #получил этот длинный ключ с сайта open weather map после регистрации

place = input("Введите, в каком городе вас интересует климат?: ")
# дальше идёт особенность модуля pyowm (читай документацию на гитхабе к модулю)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp']

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас в районе " + str(temp))