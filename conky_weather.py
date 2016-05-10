import json
import time
import os
from wu_api import WundergroundAPI

##### Edit here #####
wu_dir = '/home/xirov/projects/conky-weather-wu'
api_key = ''
country = 'Denmark'
city = 'Odense'
update_interval = 10     # in minutes
#####################


# Check when data was last pulled
cur_time = int(time.time())
with open(os.path.join(wu_dir, 'last_pull'), 'r') as last_pull_f:
    try:
        last_pull = int(last_pull_f.read().strip())
    except ValueError:
        last_pull = 0
    last_pull_f.close()

update_interval_sec = update_interval * 60

# If data was last pulled longer than the specified update interval
if last_pull + update_interval_sec < cur_time:
    # Update 'last_pull' file (containing timestamp of last pull)
    with open(os.path.join(wu_dir, 'last_pull'), 'w') as last_pull_f:
        last_pull_f.write(str(cur_time))
        last_pull_f.close()

    # Pull new data
    wuapi = WundergroundAPI(wu_dir, api_key, country, city)
    wuapi.pull()
    print('Pulled new data')

# Open wu_conditions file, and extract some data
with open(os.path.join(wu_dir, 'wu_conditions.json'), 'r') as cond_f:
    cond = json.load(cond_f)
    location = cond['location']['city']
    temp_c = cond['current_observation']['temp_c']
    wind_kph = cond['current_observation']['wind_kph']
    weather = cond['current_observation']['weather']
    wind_dir = cond['current_observation']['wind_dir']
    cur_weather_icon = cond['current_observation']['icon']
    cond_f.close()

# Open wu_astronomy file, and extract some data
with open(os.path.join(wu_dir, 'wu_astronomy.json'), 'r') as astr_f:
    astr = json.load(astr_f)
    sunset_hour = astr['sun_phase']['sunset']['hour']
    sunrise_hour = astr['sun_phase']['sunrise']['hour']
    sunset_minute = astr['sun_phase']['sunset']['minute']
    sunrise_minute = astr['sun_phase']['sunrise']['hour']
    astr_f.close()

# Open wu_forecast file, and extract some data
with open(os.path.join(wu_dir, 'wu_forecast.json'), 'r') as forc_f:
    forc = json.load(forc_f)
    #print(json.dumps(forc['forecast']['simpleforecast']['forecastday'][0], indent=4))
    day0 = forc['forecast']['simpleforecast']['forecastday'][0]
    day1 = forc['forecast']['simpleforecast']['forecastday'][1]
    day2 = forc['forecast']['simpleforecast']['forecastday'][2]
    day3 = forc['forecast']['simpleforecast']['forecastday'][3]

    pred_rain_today = day0['qpf_allday']['mm']
    pred_rain_1 = day1['qpf_allday']['mm']
    pred_rain_2 = day2['qpf_allday']['mm']
    pred_rain_3 = day3['qpf_allday']['mm']

    avewind_today = day0['avewind']['kph']
    avewind_1 = day1['avewind']['kph']
    avewind_2 = day2['avewind']['kph']
    avewind_3 = day3['avewind']['kph']

    icon1 = day1['icon']
    icon2 = day2['icon']
    icon3 = day3['icon']

    temp1_low = day1['low']['celsius']
    temp2_low = day2['low']['celsius']
    temp3_low = day3['low']['celsius']
    temp1_high = day1['high']['celsius']
    temp2_high = day2['high']['celsius']
    temp3_high = day3['high']['celsius']

    day1_name = day1['date']['weekday_short']
    day2_name = day2['date']['weekday_short']
    day3_name = day3['date']['weekday_short']


current_hour = time.strftime('%H')

icons = {
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

print('%s %d |  %s mm |  %d %s | est  %d |  %s |  %s | %s %s %s-%s/%smm | %s %s %s-%s/%smm | %s %s %s-%s/%smm' % (icons[cur_weather_icon], temp_c, pred_rain_today, wind_kph, wind_dir, avewind_today, sunrise_hour, sunset_hour, day1_name, icons[icon1], temp1_low, temp1_high, pred_rain_1, day2_name, icons[icon2], temp2_low, temp2_high, pred_rain_2, day3_name, icons[icon3], temp3_low, temp3_high, pred_rain_3))
