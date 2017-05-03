import urllib.request
import html
import re

def getWeather():
    link = "http://pogoda.74.ru/"
    file = urllib.request.urlopen(link)
    data = file.read()
    data = data.decode("UTF-8")
    file.close()
    value = re.findall(r'<span class="value__main">(.*?)</span>', str(data))
    description = re.findall(r'<span class="value-description">(.*?)</span>', str(data))
    weather = {
        'value': html.unescape(str(value[0])),
        'description' : html.unescape(str(description[0])),
    }
    return weather


