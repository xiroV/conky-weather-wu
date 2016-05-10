# Introduction
This is a weather plugin written in Python using the Wunderground API. The primary goal was to make a simple weather plugin which could be used with Conky + i3bar (Conky as an replacement to i3status), however since it's basicly just a Python script pulling weather information, you can use it however you like.

The plugin will pull weather information from [Weather Underground](https://www.wunderground.com/?apiref=7e6536cf90e4891d) every 10 minutes, and you will need your own API key from [here](https://www.wunderground.com/weather/api/).

The plugin is written using Python 3.5, and hence is also only tested with Python 3.5.

# Dependencies
- Python 3.5

  should work with any Python3.x though
- [Optional] [Weather Icons](https://erikflowers.github.io/weather-icons/)
    
    By default the script makes use of the Weather Icons (they are really pretty!), but if you don't need them, you can simply remove them from the script.

# Install
## For use with Conky
 1. Extract the contents to a directory ```dir```
 2. Modify the contents of the specified section in ```conky_weather.py```
   - ```wu_dir``` Absolute path to ```dir```
   - ```api_key``` Your API key from [Wunderground.com](https://www.wunderground.com/weather/api/). 
   - ```country``` This variable depends on wether you live in the US or not:
     - If you live in the US, this should be the 2-letter state code, e.g. ```OR``` (for Oregon), ```CA``` (for California), etc.
     - If you live in any other country than the US, this should simply be the english name of the country, e.g. ```Denmark```, ```Germany```, ```Ireland```, etc.
   - ```city``` The name of the city/area you want to get your weather data on.

   If you are unsure about what you should write for ```country``` or ```city```, try searching [Weather Underground](https://www.wunderground.com/?apiref=7e6536cf90e4891d).
 3. Insert ```{execp python ~/__dir__/conky_weather.py}``` in your ```.conkyrc```

# Configuration
Coming soon

# Additional notes
Coming soon
