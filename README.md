# NOTICE
This project have been moved to GitLab: [[https://gitlab.com/xiroV/wunderground-py]]

# News
## October 30, 2016
Realized that I had, at some point, accidentially pushed my API key to this repository, and had a reason to think that it had gotten compromised. For this reason, I regenerated my API key. If you're experiencing problems from this day, you were probably using my API key, and you should generate your own key to use data from [Weather Underground](https://www.wunderground.com/?apiref=7e6536cf90e4891d). Register for a free API key [here](https://www.wunderground.com/weather/api/).

On a more positive note, conky-weather-wu now offers configuration through a config file. I have updated this README accordingly.

Also, I'll think of a more appropriate name for this repository, since the name implies that it is only for use with conky (which is not true). Also, I'm aware of the many similar python-wunderground-like repositories on GitHub which I want to respect regarding changing the name.





# Introduction
This is a weather plugin written in Python using the Wunderground API. The primary goal was to make a simple weather plugin which could be used with Conky + i3bar (Conky as an replacement to i3status), however since it's basicly just a Python script pulling weather information, you can use it however you like.

The plugin will pull weather information from [Weather Underground](https://www.wunderground.com/?apiref=7e6536cf90e4891d) every 30 minutes (default), and you will need your own API key from [here](https://www.wunderground.com/weather/api/).

The plugin is written using Python 3.5, and hence is also only tested with Python 3.5.

# Dependencies
- Python 3.5

  should work with any Python3.x though
- [Optional] [Weather Icons](https://erikflowers.github.io/weather-icons/)
    
    By default the script makes use of the Weather Icons (they are really pretty!), but if you don't need them, you can simply remove them from the script.

# Install
 1. Extract the contents to a directory ```dir```
 2. Rename the ```config_sample``` file to ```config``` and modify accordingly:
   - ```api_key``` Your API key from [Wunderground.com](https://www.wunderground.com/weather/api/). 
   - ```country``` This variable depends on wether you live in the US or not:
     - If you live in the US, this should be the 2-letter state code, e.g. ```OR``` (for Oregon), ```CA``` (for California), etc.
     - If you live in any other country than the US, this should simply be the english name of the country, e.g. ```Denmark```, ```Germany```, ```Ireland```, etc.
   - ```city``` The name of the city/area you want to get your weather data on.

   If you are unsure about what you should write for ```country``` or ```city```, try searching [Weather Underground](https://www.wunderground.com/?apiref=7e6536cf90e4891d).

# For use with Conky
 - Insert ```{execp python ~/__dir__/conky_weather.py today}``` in your ```.conkyrc``` to get weather from today.

# Parameters
```today``` Get current degrees with a matching weather icon, e.g. ``` 8```

```today_prec``` Get precipitation for today, e.g. ``` 0 mm```

```day1``` Get tomorrows 3-letter name, icon, degree interval and precipitation, e.g. ```Mon  9-12/1mm ```

```day2``` Get the day after tomorrows 3-letter name, icon, degree interval and precipitation, e.g. ```Tue  9-12/1mm ```

```day3``` Get the 3-letter name, icon, degree interval and precipitation, e.g. ```Wed  9-12/1mm ```, for day 3.

If you want another structure (e.g. use other, or no icons), simply edit the conky_weather.py file.

# Additional Information
For any questions or requests, don't hesitate to create an issue, or contact me from http://xirov.com/contact
