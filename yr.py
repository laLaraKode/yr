import sys
from urllib2 import urlopen
import xml.etree.ElementTree as ET

url = sys.argv[1]

tree = ET.parse(urlopen(url + "/varsel.xml"))

root = tree.getroot()

place = root.find('location').find('name').text

forecast = root.find('forecast')

tabular = forecast.find('tabular')

for time in tabular.findall('time'):
	print "%s: %s-%s: %2d C, %s, %s" % (place, time.get('from'), time.get('to'), int(time.find('temperature').get('value')), time.find('symbol').get('name'), time.find('windSpeed').get('name'))

