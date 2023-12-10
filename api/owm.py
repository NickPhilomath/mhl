import logging
from django.conf import settings
from pyowm import OWM

logger = logging.getLogger(__name__)

owm = OWM(settings.OWM_API_KEY)
mgr = owm.weather_manager()

# observation = mgr.weather_at_coords(41.260555, 69.421825)
# w = observation.weather


def get_weather(lat, lng):
    try:
        observation = mgr.weather_at_coords(lat, lng)
        w = observation.weather
        return {
            "status": w.detailed_status,
            "wind": w.wind(),
            "humidity": w.humidity,
            "temp": w.temperature("celsius")["temp"],
            "clouds": w.clouds,
        }
    except Exception:
        logger.error("faced a problem while requesting weather data")
        return {}


# print(w.detailed_status)         # mist
# print(w.wind())                  # {'speed': 2.06, 'deg': 320}
# print(w.humidity)                #  76
# print(w.temperature('celsius'))  # {'temp': 8.77, 'temp_max': 8.77, 'temp_min': 8.77, 'feels_like': 7.71, 'temp_kf': None}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75
