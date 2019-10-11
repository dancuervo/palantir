""" Clase para obtener datos de url
 https://docs.python.org/3/library/urllib.html

los datos llegan en formato xml
desde 
https://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados

https://timestamp.online/article/how-to-get-current-timestamp-in-python
https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
https://www.geeksforgeeks.org/comparing-dates-python/
"""
import urllib.request

from datetime import datetime

from pathlib import Path

class obtenerDatos:
    
    def __init__(self):
        self.origen = 'https://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados'
        self.destino = 'archivos'
        dateTimeObj = datetime.now()
        self.timestamp = dateTimeObj.strftime("%Y-%m-%d")
        self.stamp = Path(self.destino).joinpath(self.timestamp)
    
    def obtener(self):
        return urllib.request.urlretrieve(self.origen,self.stamp)

deputados_xml = obtenerDatos()
deputados_xml.obtener()