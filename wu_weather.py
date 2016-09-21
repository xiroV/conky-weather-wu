import time
import os
import json
from wu_api import WundergroundAPI

class WUWeather():
    """ Weather Underground Class """

    def __init__(self):
        # Loading config file
        wu_weather_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(wu_weather_path, 'config')

        try:
            with open(config_path, 'r') as config_f:
                config_read = json.load(config_f)

                config = dict()

                # Config defaults:
                config['api_key'] = None
                config['country'] = 'Denmark'
                config['city'] = 'Odense'
                config['update_interval_minutes'] = 10
                config['temp_units'] = 'C'    # C or F
                config['speed_units'] = 'KPH' # KPH or MPH
                config['length_units'] = 'MM' # MM or INCH


                for user_conf in config_read:
                    config[user_conf] = config_read[user_conf]

        except FileNotFoundError:
            print("Error: Could not locate the config file: ", config_path)
            exit()

        self.wind_speed = {}
        self.day_name = {}
        self.icon = {}
        self.day_name_short = {}
        self.precipitation = {}
        self.conditions = {}
        self.temp_high = {}
        self.temp_low = {}

        # Check when data was last pulled
        cur_time = int(time.time())
        with open(os.path.join(wu_weather_path, 'last_pull'), 'r') as last_pull_f:
            try:
                last_pull = int(last_pull_f.read().strip())
            except ValueError:
                last_pull = 0
            last_pull_f.close()

        update_interval_sec = config['update_interval_minutes'] * 60

        # If data was last pulled longer than the specified update interval
        if last_pull + update_interval_sec < cur_time:
            # Update 'last_pull' file (containing timestamp of last pull)
            with open(os.path.join(wu_weather_path, 'last_pull'), 'w') as last_pull_f:
                last_pull_f.write(str(cur_time))
                last_pull_f.close()

            # Pull new data
            wuapi = WundergroundAPI(wu_weather_path, config['api_key'], config['country'], config['city'])
            wuapi.pull()


        # Open wu_conditions file, and extract some data
        with open(os.path.join(wu_weather_path, 'wu_conditions.json'), 'r') as cond_f:
            cond = json.load(cond_f)
            self.city = cond['location']['city']

            # Get temperature in units for current day
            if config['temp_units'] == 'C':
                self.temperature = cond['current_observation']['temp_c']
            else:
                self.temperature = cond['current_observation']['temp_f']

            if config['speed_units'] == 'KPH':
                self.wind_speed[0] = cond['current_observation']['wind_kph']
            else:
                self.wind_speed[0] = cond['current_observation']['wind_mph']

            self.conditions[0] = cond['current_observation']['weather']

            self.wind_direction = cond['current_observation']['wind_dir']
            self.icon[0] = cond['current_observation']['icon']
            cond_f.close()

        # Open wu_astronomy file, and extract some data
        with open(os.path.join(wu_weather_path, 'wu_astronomy.json'), 'r') as astr_f:
            astr = json.load(astr_f)
            self.sunset_hour = astr['sun_phase']['sunset']['hour']
            self.sunrise_hour = astr['sun_phase']['sunrise']['hour']
            self.sunset_minute = astr['sun_phase']['sunset']['minute']
            self.sunrise_minute = astr['sun_phase']['sunrise']['hour']
            astr_f.close()

        # Open wu_forecast file, and extract some data
        with open(os.path.join(wu_weather_path, 'wu_forecast.json'), 'r') as forc_f:
            forc = json.load(forc_f)
            forecast = forc['forecast']['simpleforecast']['forecastday']

            for day in range(0,4):
                self.precipitation[day] = forecast[day]['qpf_allday']['mm']

            if config['speed_units'] == 'KPH':
                for day in range(0,4):
                    self.wind_speed[day] = forecast[day]['avewind']['kph']
            else:
                for day in range(0,4):
                    self.wind_speed[day] = forecast[day]['avewind']['mph']


            for day in range(1,4):
                self.icon[day] = forecast[day]['icon']

            if config['temp_units'] == 'C':
                for day in range(0,4):
                    self.temp_high[day] = forecast[day]['high']['celsius']
                    self.temp_low[day] = forecast[day]['low']['celsius']
            else:
                for day in range(0,4):
                    self.temp_high[day] = forecast[day]['high']['fahrenheit']
                    self.temp_low[day] = forecast[day]['low']['fahrenheit']
                
            for day in range(0,4):
                self.day_name_short[day] = forecast[day]['date']['weekday_short']

            forc_f.close()


        current_hour = time.strftime('%H')


        self.icons = {
            'chanceflurries':'',
            'chancerain':'',
            'chancesleet':'',
            'chancesnow':'',
            'chancetstorms':'',
            'clear':'',
            'cloudy':'',
            'flurries':'',
            'fog':'',
            'hazy':'',
            'mostlycloudy':'',
            'mostlysunny':'',
            'partlycloudy':'',
            'partlysunny':'',
            'sleet':'',
            'rain':'',
            'snow':'',
            'sunny':'',
            'tstorms':'',
            'nt_chanceflurries':'',
            'nt_chancerain':'',
            'nt_chancesleet':'',
            'nt_chancesnow':'',
            'nt_chancetstorms':'',
            'nt_clear':'',
            'nt_cloudy':'',
            'nt_flurries':'',
            'nt_fog':'',
            'nt_hazy':'',
            'nt_mostlycloudy':'',
            'nt_mostlysunny':'',
            'nt_partlycloudy':'',
            'nt_partlysunny':'',
            'nt_sleet':'',
            'nt_rain':'',
            'nt_snow':'',
            'nt_sunny':'',
            'nt_tstorms':''
        }


    def get_temperature(self):
        return self.temperature

    def get_temp_low(self, day=0):
        return self.temp_low[day]

    def get_temp_high(self, day=0):
        return self.temp_high[day]

    def get_wind_speed(self, day = 0):
        return self.wind_speed[0]

    def get_wind_direction(self):
        return self.wind_direction

    def get_precipitation(self, day = 0):
        return self.precipitation[day]

    def get_day_name(self, day = 0):
        pass

    def get_day_name_short(self, day = 0):
        return self.day_name_short[day]

    def get_sunset_hour(self, day = 0):
        return self.sunset_hour

    def get_sunrise_hour(self, day = 0):
        return self.sunrise_hour

    def get_icon(self, day = 0):
        return self.icons[self.icon[day]]
