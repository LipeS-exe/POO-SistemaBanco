from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime as dt
from uuid import uuid4 as id

class Cliente:
    def __init__(self, endereco , contas):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoalFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
        def __init__(self, numero , clinte) :
            self._saldo = 0
            self._numero = numero
            self._agencia = str(id.uuid4())
            self._cliente = cliente
            self._historico = Historico()

        @classmethod
        def saldo(self):
            return self._saldo
        
        @property
        def numero(self):
            return self._numero
        
        @property
        def agencia(self):
            return self._agencia
        
        @property
        def cliente(self):
            return self._cliente
        
        @property
        def historico(self):
            return self._historico
        def sacar(self, valor)
            

class ContaCorrente(conta):

class Historico:

class Transacao(ABC):
    
class Saque(Transacao):

class Deposito(Transacao):