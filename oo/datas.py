class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return print(str(self.dia) + '/' + str(self.mes) + '/' + str(self.ano))


if __name__ == '__main__':
    d = Data(21, 11, 2007)
    d.formatada()
