from utils import titulo, limpar_terminal, confirma_login, printar_eventos, criar_data, criar_aluno, criar_organizador, verificaUserType
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
        if verificaUserType(usuario):
            titulo("Sistema do Organizador")

            print("[1] - Criar Eventos")
            print("[2] - Atualizar Eventos")
            print("[3] - Atualizar Status de um Evento")
            print("[4] - Excluir Evento")
            print("[5] - Visualizar a lista de inscritos em seu evento")
            print("[999] - Sair")

            escolha_usuario = input("Sua escolha: ")
            
            if escolha_usuario == "999":
                usuario = None
            elif escolha_usuario == "1": # ------- Criando Evento ---------- #
                titulo("Criando Eventos")
                try:
                    msg_evento = usuario.criarEvento(eventos)
                    print(msg_evento)
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
                                print(usuario.cancelarEvento(evento))
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
                            print(usuario.deletarEvento(eventos, evento))
                            sleep(2)
                except:
                    print("Dados inválidos!")
                    sleep(2)

            elif escolha_usuario == '5': # ------------------- lista de inscritos em seus eventos ------------------ #
                titulo("Seus eventos")
                for evento in eventos:
                    if evento.idOrganizador == usuario.idUsuario:
                        printar_eventos(evento)
                
                try:
                    escolha_usuario = int(input("ID do evento que deseja: "))
                    for evento in eventos:
                        if evento.idEvento == escolha_usuario:
                            if evento.idOrganizador == usuario.idUsuario:

                                titulo("Alunos inscritos")
                                for aluno in evento.alunosInscritos:
                                    print(f"{'RA:':<25} {aluno.RA:<45}")
                                    print(f"{'Nome:':<25} {aluno.nome:<45}")
                                    print(f"{'Curso:':<25} {aluno.curso:<45}")
                                    print("_-" * 60)
                                    print()
                                
                                input("Pressione 'Enter' para voltar!")
                                break

                            else:
                                print("Esse evento não foi criado por você!")
                                sleep(2)
                                break
                except:
                    print("Dados inválidos!")
                    sleep(2)
                
            else:
                print("Escolha inválida!")
                sleep(2)
        
        # ------------------------------------ Sistema do Aluno ------------------------------------ #
        elif verificaUserType(usuario, organizador=False, aluno=True):
            titulo("Sistema do Aluno")

            print("[1] - Inscrever-se em eventos")
            print("[2] - Cancelar inscrição em eventos")
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
                            print(usuario.inscreverseNoEvento(evento))
                            sleep(2)
                except:
                    print("Dados inválidos!!")
                    sleep(2)

            elif escolha_usuario == "2": # ----------------------- Cancelamento de inscrição ---------------------- #
                for evento in eventos:
                    if evento.status == "Ativo": #Verifica se o evento está ativo
                        printar_eventos(evento)
                try:
                    escolha_usuario = int(input("ID do Evento que deseja inscrever-se: "))
                    for evento in eventos:
                        if evento.idEvento == escolha_usuario and evento.status == "Ativo":
                            print(usuario.desinscreverseNoEvento(evento))
                            sleep(2)
                except:
                    print("Dados inválidos!!")
                    sleep(2)
            
            else:
                print("Escolha inválida!")
                sleep(2)