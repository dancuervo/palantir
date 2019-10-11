""""clase para convertir xml para json
https://stackabuse.com/reading-and-writing-xml-files-in-python/
https://pypi.org/project/xmljson/
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, tostring, fromstring, parse
from xmljson import parker
import json
from json import dumps
from pathlib import Path

origen = 'archivos'
timestamp = '2019-10-07'
origen = Path( origen ).joinpath( timestamp )
archivo = parse(origen)

print(archivo)
#parker.data
