from bs4 import Beautifulsoup 
import requests
import html5lib
# import os

url ="https://www.timeanddate.com/weather/netherlands/delft"

response =requests.get(url)

result =Beautifulsoup(response.content,"html5lib")

temperature_raw_data = result.findall('td')[12]

temperature = temperature_raw_data.get_text()

print('Temperature of Delft city :',temperature)