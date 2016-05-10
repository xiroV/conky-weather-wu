import urllib.request
import json
import os

class WundergroundAPI(object):
    def __init__(self, local_path, api_key, country, city):
        self.local_path = local_path
        self.api_key = api_key
        self.country = country
        self.city = city

    # Pull data from Wunderground
    def pull(self):
        with urllib.request.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/conditions/q/' + self.country + '/' + self.city + '.json') as c:
            # Save weather condition data
            with open(os.path.join(self.local_path, 'wu_conditions.json'), 'w') as conditions_file:
                conditions_file.write(c.read().decode('utf-8'))
                conditions_file.close()
            c.close()

        with urllib.request.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/astronomy/q/' + self.country + '/' + self.city + '.json') as a:
            # Save astronomy data
            with open(os.path.join(self.local_path, 'wu_astronomy.json'), 'w') as astronomy_file:
                astronomy_file.write(a.read().decode('utf-8'))
                astronomy_file.close()
            a.close()

        with urllib.request.urlopen('http://api.wunderground.com/api/' + self.api_key + '/geolookup/forecast/q/' + self.country + '/' + self.city + '.json') as f:
            # Save astronomy data
            with open(os.path.join(self.local_path, 'wu_forecast.json'), 'w') as forecast_file:
                forecast_file.write(f.read().decode('utf-8'))
                forecast_file.close()
            f.close()

