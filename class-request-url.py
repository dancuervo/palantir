# clasee RequerirURL realizar un httpRequest
# query guarda la finalidad del request - hacia dónde se realiza
# url -url del request

class RequerirURL:
    def __init__ (self, query, url):
        self.query = query
        self.url = url

    def reqURL(self):
        
        from urllib import request
        consulta = request.urlopen(self.url)
        resultado = consulta.read()

        #archivando los datos en un archivo con timestamp
        from time import gmtime, strftime
        strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        'Thu, 28 Jun 2001 14:17:15 +0000'

        resultado_string = resultado.decode("utf-8")
        archivar = open("./archivo/archivado " + self.query + " " + strftime("%Y %b %d %H:%M:%S", gmtime()) + ".txt", "w")
        archivar.write(resultado_string)
        archivar.close()

#prueba = RequerirURL("diputados","https://www.camara.leg.br/SitCamaraWS/Deputados.asmx/ObterDeputados")
#prueba.reqURL()

class ConvertirXMLtoJSON:
    def __init__(self,origen):
        self.origen = origen
        self.archivo = "./archivo/" + self.origen
    def convertir(self):

        import json
        #pip install xmltodict https://pypi.org/project/xmltodict/
        import xmltodict

        with open(self.archivo, 'r') as entrada:
            xmlString = entrada.read()

        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
        
        #archivando los datos en un archivo con timestamp
        from time import gmtime, strftime
        strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        archivar = open("./archivo/archivado " + self.origen + strftime("%Y %b %d %H:%M:%S", gmtime()) + ".JSON", "w")
        archivar.write(jsonString)
        archivar.close()
        
        

prueba = ConvertirXMLtoJSON("archivado.txt")
print(prueba.convertir())