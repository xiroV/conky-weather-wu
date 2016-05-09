import urllib.request
import json
import os

class WundergroundAPI(object):
    def __init__(self, path):
        self.path = path

    def pull(self):
        with urllib.request.urlopen('http://api.wunderground.com/api/b2fd9cf3d2750fc7/geolookup/conditions/q/Denmark/Odense.json') as c:
            # Save data
            with open(os.path.join(self.path, 'wu_conditions.json'), 'w') as conditions_file:
                conditions_file.write(c.read().decode('utf-8'))
                conditions_file.close()
            c.close()

        with urllib.request.urlopen('http://api.wunderground.com/api/b2fd9cf3d2750fc7/geolookup/astronomy/q/Denmark/Odense.json') as a:
            with open(os.path.join(self.path, 'wu_astronomy.json'), 'w') as astronomy_file:
                astronomy_file.write(a.read().decode('utf-8'))
                astronomy_file.close()
            a.close()
