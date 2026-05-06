from abc import ABC, abstractmethod
from datetime import datetime as dt
from uuid import uuid4

# ================= CLIENTE =================
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


# ================= CONTA =================
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = str(uuid4())
        self._cliente = cliente
        self._historico = Historico()

    @property
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
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False

        if valor <= 0:
            print("Valor inválido.")
            return False

        self._saldo -= valor
        print("Saque realizado.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False

        self._saldo += valor
        print("Depósito realizado.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques = len([
            t for t in self.historico.transacoes
            if t["tipo"] == "Saque"
        ])

        if valor > self.limite:
            print("Excedeu limite por saque.")
            return False

        if saques >= self.limite_saques:
            print("Excedeu número de saques.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
Agência: {self.agencia}
Conta: {self.numero}
Titular: {self.cliente.nome}
"""


# ================= HISTORICO =================
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": dt.now().strftime("%d-%m-%Y %H:%M:%S")
        })


# ================= TRANSACOES =================
class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)