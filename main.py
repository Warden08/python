import eel
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM('e5e30cfb3f732f42b5ed32d90ffb0489', config_dict  )

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return "In city " + place + " right now " + str(temp) + " degrees!"

eel.init("C:/Users/velic/5/web")
eel.start("main.html",size=(450,450))