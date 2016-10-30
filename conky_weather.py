from wu_weather import WUWeather
import sys

weather = WUWeather()

for arg in sys.argv:
    if arg == "today":
        print('  %s %d  ' % (weather.get_icon(), weather.get_temperature()))
    if arg == "today_prec":
        print('   %s mm  ' % (weather.get_precipitation()))
    if arg == "day1":
        print('  %s %s %s-%s/%smm  ' % (weather.get_day_name_short(1), weather.get_icon(1), weather.get_temp_low(1), weather.get_temp_high(1), weather.get_precipitation(1)))
    if arg == "day2":
        print('  %s %s %s-%s/%smm  ' % (weather.get_day_name_short(2), weather.get_icon(2), weather.get_temp_low(2), weather.get_temp_high(2), weather.get_precipitation(2)))
    if arg == "day3":
        print('  %s %s %s-%s/%smm  ' % (weather.get_day_name_short(3), weather.get_icon(3), weather.get_temp_low(3), weather.get_temp_high(3), weather.get_precipitation(3)))
