class operateJSON:
    def __init__ (self, origen):
        self.origen = origen
        self.archivo = './archivo/' + self.origen

    def list_entries(self):

       # print(locals())
        import json
        with open(self.archivo,'r') as json_file:
            data = json.load(json_file)
            
            #from pprint import pprint
            #pprint(locals())

            deputado = data['deputados']['deputado']
            deputado_lenght = len(data['deputados']['deputado'])
            i = 0
            while i < deputado_lenght:
                print(deputado[i]['nome'])
                print(deputado[i]['ideCadastro'])
                i += 1


consulta = operateJSON("archivado.JSON")
print(consulta.list_entries())