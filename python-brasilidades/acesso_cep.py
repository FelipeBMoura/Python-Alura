import requests


class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def format_cep(self):
        return f"{self.cep[:4]}-{self.cep[5:]}"

    @staticmethod
    def cep_e_valido(cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf'],
        )
