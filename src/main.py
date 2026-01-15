from models import *
from models.Evento import Evento
from utils import *

from datetime import date
from time import sleep

usuarios = []
eventos = []

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
    
    # ----------------------- Sistemas ----------------------- #
    if usuario != None:

        # ---------------------------------- Sistema do Organizador ---------------------------- #
        if isinstance(usuario, Organizador):
            titulo("Organizador")

            print("[1] - Criar Eventos")
            print("[2] - Atualizar Eventos")
            print("[3] - Atualizar Status de um Evento")
            print("[999] - Sair")

            escolha_usuario = input("Sua escolha: ")
            
            if escolha_usuario == "999":
                parar = True
            elif escolha_usuario == "1": # ------- Criando Evento ---------- #
                titulo("Criando Eventos")
                try:
                    nome = input("Nome: ")
                    print("Data do evento")
                    data = criar_data()
                    descricao = input("Descrição: ")
                    max_participantes = int(input("Número máximo de participantes: "))

                    evento = Evento(len(eventos) + 50000, usuario.idUsuario, nome, data, descricao, max_participantes)
                    eventos.append(evento)
                    print("Evento criado com sucesso!")
                    sleep(2)
                except ValueError:
                    print("dados inválidos!!")
                    sleep(2)
            
            elif escolha_usuario == "2": # ---------- Atualizando Eventos ---------- #
                titulo("Atualizando Eventos")
                try:
                    for evento in eventos:
                        printar_eventos(evento)

                    escolha_usuario = input("ID do evento que deseja atualizar: ")
                    for evento in eventos:
                        if evento.idEvento == int(escolha_usuario):
                            printar_eventos(evento)
                            
                            print("Data do evento")
                            data = criar_data()
                            max_participantes = int(input("Número máximo de participantes: "))

                            evento.data = data
                            evento.numeroMaxParticipantes = max_participantes
                            print("Evento atualizado com sucesso!!")
                            sleep(2)
                            break
                except ValueError:
                    print("Dados inválidos!!")
                    sleep(2)