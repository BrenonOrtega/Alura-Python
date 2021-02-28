class Data:
    def __init__ (self, dia, mes, ano):
        self.dia = dia
        self.mes = mes 
        self.ano = ano
    
    def formatada(self):     
        self.data_formatada = f"{self.dia}/{self.mes}/{self.ano}"
        print (self.data_formatada)

