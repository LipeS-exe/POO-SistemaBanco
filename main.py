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
        
        def sacar(self, valor):
            saldo = self.saldo
            execedeu_saldo = valor > saldo

            if execedeu_saldo:
                print("\n--- Operação Falhou! Você não tem saldo suficiente.")
            elif valor > 0:
                self._saldo -=valor
                print("\n--- Saque Realizado com sucesso!")
                return True
            else:
                print("\n Operação falhou! o valor informado é invalido.")
            return False
        def depositar(self,valor):
            if valor > 0:
                self._saldo += valor
                print("\n Depósito realizado com sucesso!")
            else:
                print("--- Operação falhou! o valor informado é inválido")
                return False
            return True


class ContaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numeros_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__]
        )
        execedeu_limite = valor > self.limite
        execedeu_saques = numeros_saques > self.limite_saques

        if execedeu_limite:
            print("\n Operação falhou! o valor do saque excede o limite.")

        elif execedeu_saques:
            print("\n Operação falhou! Número máxímo de saques excedido.")

        else:
            return super().sacar(valor)
        return False
    
        def __str__(self):
            return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

# 0925

class Historico:

class Transacao(ABC):
    
class Saque(Transacao):

class Deposito(Transacao):