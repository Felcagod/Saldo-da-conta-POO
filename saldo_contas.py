import os 
from os import * 
import time
from time import sleep 

#funcoes de estetica
def linhas():
    print("-="*11)
def limpar_tela():
    #system("clear") #caso esteja ultilizando linux 
    system("cls")

#criando a classe da conta
class ContaCorrente():

    def __init__(self, num_conta, nome_usuario, saldo):
        self.num_conta = num_conta
        self.nome_usuario = nome_usuario
        self.saldo = saldo

    #alterar o nome do usuario
    def alterar_nome(self, nome_usuario):
        self.nome_usuario = nome_usuario

    #Acrescentar credito na conta
    def deposito(self, acrescentar):
        self.saldo = self.saldo + acrescentar

    #Sacar credito na conta
    def saque(self, dinheiro_a_menos):
        self.saldo = self.saldo - dinheiro_a_menos 

#input de infomacoes principais    
system("cls")
num_conta = input("Numero da conta: ")
nome_usuario = input('Nome: ')
nome_usuario = nome_usuario.capitalize()
saldo = float(input("Saldo: ")) 

conta = ContaCorrente(num_conta,nome_usuario,saldo ) #objeto conta

limpar_tela()
cont = 0

#loopign para o programa principal 
while True:

    if cont <= 0:

        linhas()
        print("Oque quer fazer? ")
        linhas()

    print("1. alterar nome")
    print("2. deposito")
    print("3. saque")
    print("4. Informacoes conta")
    print("5. sair")
    acao = int(input(": "))
    system("cls")


    if acao == 1:#acao para mudar o nome da conta
        global novo_nome 
        novo_nome = input("novo nome: ") 
        conta.alterar_nome(novo_nome)
        limpar_tela()
        print("---NOME MUDADO COM SUCESSO---")
        sleep(2)
        limpar_tela()
        cont+=1

    elif acao == 2:#acao de deposito na conta
        cont+=1
        global acrescentar 
        acrescentar = float(input("Quantida: "))
        conta.deposito(acrescentar)
        limpar_tela()
        linhas()
        print("---DEPOSITO FEITO COM SUCESSO")
        linhas()
        sleep(2)
        limpar_tela()

    elif acao ==3:#acao de saque da conta
        cont+=1
        global dinheiro_a_menos 
        dinheiro_a_menos = float(input("Quantia: "))
        conta.saque(dinheiro_a_menos)
        limpar_tela()
        linhas()
        print("---SAQUE FEITO COM SUCESSO---")
        linhas()
        sleep(2)
        limpar_tela()

    elif acao == 4:#exibir todas as informacoes do usuario
        cont+=1
        linhas()
        print("Nome:",conta.nome_usuario)
        print("Numero da conta:",conta.num_conta)
        print("Saldo: R$%.2f"%conta.saldo)
        linhas()

    elif acao == 5:#fechando o programa 
        break 

    else:
        cont+=1
        linhas()
        print("Opcao inexistente. Tente novamente!")
        linhas()


        

        