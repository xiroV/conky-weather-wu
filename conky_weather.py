from wu_weather import WUWeather

weather = WUWeather()

print('%s %d    %s mm    %d %s    %s-%s   %s %s %s-%s/%smm   %s %s %s-%s/%smm   %s %s %s-%s/%smm' % (weather.get_icon(), weather.get_temperature(), weather.get_precipitation(), weather.get_wind_speed(), weather.get_wind_direction(), weather.get_sunrise_hour(), weather.get_sunset_hour(), weather.get_day_name_short(1), weather.get_icon(1), weather.get_temp_low(1), weather.get_temp_high(1), weather.get_precipitation(1), weather.get_day_name_short(2), weather.get_icon(2), weather.get_temp_low(2), weather.get_temp_high(2), weather.get_precipitation(2), weather.get_day_name_short(3), weather.get_icon(3), weather.get_temp_low(3), weather.get_temp_high(3), weather.get_precipitation(3)))
