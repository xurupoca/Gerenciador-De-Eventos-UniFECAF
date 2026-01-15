import os

from models import *
from utils import *

from datetime import date
from time import sleep

usuarios = []

usuario = None

parar = False

while parar != True:
    limpar_terminal()

    titulo("Gerenciador de Eventos")

    # Inicial
    if usuario == None:
        print("[1] - Criar conta")
        print("[2] - Logar")
        print("[3] - Sair")

        escolha_usuario = input("Sua escolha: ")

        # Cadastros
        if escolha_usuario == "1":
            print("[1] - Organizador")
            print("[2] - Aluno")
            print("[3] - Voltar")

            escolha_usuario = input("Sua escolha: ")

            if escolha_usuario == "1":
                criar_organizador(usuarios)

            if escolha_usuario == "2":
                criar_aluno(usuarios)

        # Login de Usuarios
        elif escolha_usuario == "2":
            titulo("Login")
            email = input("E-mail: ")
            senha = input("Senha: ")

            usuario = confirma_login(usuarios, email, senha)

        elif escolha_usuario == "3":
            parar = True
        
        else:
            print("Digite um número válido!")
            sleep(2)