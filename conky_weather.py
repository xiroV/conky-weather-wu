import json
import time
import os
from wu_api import WundergroundAPI

##### Edit here #####
wu_dir = '/home/xirov/projects/i3conky-weather'
api_key = 'b2fd9cf3d2750fc7'
country = 'Denmark'
city = 'Odense'
#####################


cur_time = time.time()
with open(os.path.join(wu_dir, 'last_pull'), 'r') as last_pull_f:
    try:
        last_pull = float(last_pull_f.read().strip())
    except ValueError:
        last_pull = 0.0
    last_pull_f.close()

if last_pull + 600 < cur_time:

    with open(os.path.join(wu_dir, 'last_pull'), 'w') as last_pull_f:
        last_pull_f.write(str(cur_time))
        last_pull_f.close()

    # Pull new data
    wuapi = WundergroundAPI(wu_dir, api_key, country, city)
    wuapi.pull()

with open(os.path.join(wu_dir, 'wu_conditions.json'), 'r') as cond_f:
    data = json.load(cond_f)
    #print(json.dumps(data, sort_keys=True, indent=4))
    location = data['location']['city']
    temp_c = data['current_observation']['temp_c']
    wind_kph = data['current_observation']['wind_kph']
    weather = data['current_observation']['weather']
    wind_dir = data['current_observation']['wind_dir']
    cond_f.close()

    with open(os.path.join(wu_dir, 'wu_astronomy.json'), 'r') as astr_f:
        astr = json.load(astr_f)
        sunset_hour = astr['sun_phase']['sunset']['hour']
        sunrise_hour = astr['sun_phase']['sunrise']['hour']
        sunset_minute = astr['sun_phase']['sunset']['minute']
        sunrise_minute = astr['sun_phase']['sunrise']['hour']
        #print(astr['moon_phase'])
        astr_f.close()

current_hour = time.strftime('%H')

icons_day = ['', '', '', '', '', '', '', '', '']
icons_night = ['', '', '', '', '', '', '', '', '']

if current_hour > sunset_hour and current_hour < sunrise_hour:
    icons = icons_night
else:
    icons = icons_day

if weather == 'Clear':
    icon = icons[0]
elif weather == 'Scattered Clouds':
    icon = icons[1]
elif weather == 'Partly Cloudy':
    icon = icons[1]
elif weather == 'Mostly Cloudy':
    icon = icons[2]
elif weather == 'Chance of Rain':
    icon = icons[3]
elif weather == 'Overcast':
    icon = icons[4]
elif weather == 'Rain':
    icon = icons[5]
elif weather == 'Snow':
    icon = icons[6]
elif weather == 'Fog':
    icon = icons[7]
elif weather == 'Thunderstorms with Hail':
    icon = icons[8]
elif weather == 'Tstorm':
    icon = icons[8]
else:
    icon = weather

print('%s %d     %d %s      %s ~ %s ' % (icon, temp_c, wind_kph, wind_dir, sunrise_hour, sunset_hour))
