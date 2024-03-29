from abc import ABCMeta, abstractmethod
from audioop import reverse


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'[>>Código {self._codigo} Saldo {self._saldo}<<]'


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


# ContaInvestimento(17) # Não roda pois falta implementar o método abstrato da classe abstrata

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(conta)

import array as arr

# evitamos usaar array puro. Paddrão é usar Numpy
print(arr.array('d', [1, 3.5]))  # 'd' significa double, conforme documentação

# print(arr.array('d', [1, 3.5, "Guilherme"]))

import numpy as np

numeros = np.array([[1, 3.5]])

print(numeros)

numeros = numeros + 3

print(numeros)


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Código {self._codigo} Saldo {self._saldo}<<]'


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaCorrente(37)
print(conta2)

print(conta1 == conta2)

contas = [conta1]

print(conta1 in contas)

print(conta1 in [conta2])

print(conta2 in [conta1])

print(conta2 in contas)

idades = [15, 87, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))

print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, 'x' , idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979),
]

for nome, idade, nascimento in usuarios:
    print(nome)

print(sorted(idades))

print(list(reversed(idades)))

print(sorted(idades, reverse=True))

idades.sort()

print(idades)

print(15 < 32)

nomes = ['guilherme', 'Daniela', 'paulo']
print(sorted(nomes))

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print(conta_do_guilherme < conta_da_daniela)

print(conta_do_guilherme > conta_da_daniela)

for conta in sorted(contas):
    print(conta)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo

        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'[>>Código {self._codigo} Saldo {self._saldo}<<]'

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
    print(conta)

print(conta_do_guilherme <= conta_da_daniela)

print(conta_do_guilherme <= conta_do_paulo)
