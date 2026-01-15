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
            titulo("Sistema do Organizador")

            print("[1] - Criar Eventos")
            print("[2] - Atualizar Eventos")
            print("[3] - Atualizar Status de um Evento")
            print("[4] - Excluir Evento")
            print("[999] - Sair")

            escolha_usuario = input("Sua escolha: ")
            
            if escolha_usuario == "999":
                usuario = None
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
            
            elif escolha_usuario == "3": # ------------- Atualizar Status Evento ----------- #
                titulo("Atualizar Status de Eventos")
                for evento in eventos:
                    printar_eventos(evento)
                try:
                    escolha_usuario = input("ID do Evento: ")
                    for evento in eventos:
                        if evento.idEvento == int(escolha_usuario):
                    
                            print("[1] - Ativo")
                            print("[2] - Cancelado")
                            print("[3] - Concluído")
                            escolha_usuario = input("Sua escolha: ")

                            if escolha_usuario == "1":
                                evento.status = "Ativo"
                                print("Status atualizado!!")
                                sleep(2)
                            elif escolha_usuario == "2":
                                evento.status = "Cancelado"
                                print(f"Status atualizado!! {evento.status}")
                                sleep(2)
                            elif escolha_usuario == "3":
                                evento.status = "Concluido"
                                print("Status atualizado!!")
                                sleep(2)
                            else:
                                print("Escolha inválida!!")
                                sleep(2)
                except:
                    print("Dados inválidos!")
                    sleep(2)

            elif escolha_usuario == "4": # ------------------ Excluir Evento ------------- #
                titulo("Excluir Evento")
                for evento in eventos:
                    print(evento.status)
                    if evento.status == "Cancelado":
                        printar_eventos(evento)
                try:
                    escolha_usuario = input("ID do evento que deseja excluir: ")
                    for evento in eventos:
                        if evento.idEvento == int(escolha_usuario):
                            if evento.status == "Cancelado":
                                eventos.remove(evento)
                                print("Evento excluido com sucesso!")
                                sleep(2)
                            else:
                                print("Evento não pode ser removido!")
                                sleep(2)
                except:
                    print("Dados inválidos!")
                    sleep(2)
            
            else:
                print("Escolha inválida!")
                sleep(2)
        
        # ------------------------------------ Sistema do Aluno ------------------------------------ #
        elif isinstance(usuario, Aluno):
            titulo("Sistema do Aluno")

            print("[1] - Inscrever-se em eventos")
            print("[999] - Sair")

            escolha_usuario = input("Sua escolha: ")
            if escolha_usuario == "999":
                usuario = None
            elif escolha_usuario == "1": # ------------------------- Inscrição em eventos ------------------ #
                for evento in eventos:
                    if evento.status == "Ativo": #Verifica se o evento está ativo
                        printar_eventos(evento)
                try:
                    escolha_usuario = int(input("ID do Evento que deseja inscrever-se: "))
                    for evento in eventos:
                        if evento.idEvento == escolha_usuario and evento.status == "Ativo":
                            if len(evento.alunosInscritos) > 0:
                                for inscrito in evento.alunosInscritos:
                                    if inscrito.RA == usuario.RA: # Verifica se o aluno já não está inscrito
                                        print("Já está inscrito neste evento!")
                                        sleep(2)
                                    else:
                                        evento.alunosInscritos.append(usuario)
                                        print("Inscrição realizada!")
                                        sleep(2)
                            else:
                                evento.alunosInscritos.append(usuario)
                                print("Inscrição realizada!")
                                sleep(2)
                except:
                    print("Dados inválidos!!")
                    sleep(2)
            
            else:
                print("Escolha inválida!")
                sleep(2)