import os
import platform
from datetime import date
from time import sleep
import csv
from fpdf import FPDF

from models.Aluno import Aluno
from models.Organizador import Organizador

def limpar_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:  # Linux e macOS
        os.system("clear")

def titulo(titulo: str):
    limpar_terminal()
    if isinstance(titulo, str):
        print("_-" * 60)
        print(f"{titulo:^120}")
        print("_-" * 60)
        print()

    else:
        raise ValueError("título deve ser str")

def coleta_de_dados_usuarios() ->dict:
    """
    Coleta os dados de cadastro de Usuário
    
    :return: Retorna os dados coletados
    :rtype: dict
    """
    # Coleta de dados
    nome = input("Nome: ")
    senha = input("Senha: ")
    print("Data de Nascimento")
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")

    dataDeNascimento = date(int(ano), int(mes), int(dia))

    email = input("E-mail: ")
    dataDeCadastro = date.today()

    return {"nome": nome, "senha": senha, "dataDeNascimento": dataDeNascimento, "email": email, "dataDeCadastro": dataDeCadastro}

def confirma_login(usuarios: list, email: str, senha: str) -> object:
    """
    Confirma o login do usuário
    
    :param usuarios: lista com os usuários cadastrados
    :type usuarios: list
    :param email: email do usuário
    :type usuarios: str
    :param senha: senha do usuário
    :type usuarios: str
    :return: retorna o usuário logado ou None se falhar
    :rtype: object
    """

    for item in usuarios:
        if item.VerificarLogin(email, senha):
            print("Login efetuado com sucesso!")
            sleep(2)
            return item
    print("Dados inválidos!")
    sleep(2)
    return None


def csv_export(data: list, file_name: str) -> True:
    """
    Exporta os dados em CSV

    :param data: Dados em lista para exportação
    :type data: list
    :param file_name: Nome do arquivo a ser gerado
    :type file_name: str
    :return: True se criado com sucesso
    :rtype: bool
    """
    with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(data)
    return True

def pdf_export(data: list, file_name: str) -> True:
    """
    Exporta os dados em PDF

    :param data: Dados em lista para exportação
    :type data: list
    :param file_name: Nome do arquivo a ser gerado
    :type file_name: str
    :return: True se criado com sucesso
    :rtype: bool
    """
    

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for cell in data:
        texto = ""
        for item in cell:
            texto + " - " + str(item)
        pdf.cell(200, 10, txt=texto, ln=True, align="C")

    pdf.output(f"{file_name}.pdf")
    return True

def printar_eventos(evento: object):
    """
    Printa um evento detalhado

    :param evento: Objeto do tipo Evento
    :type evento: object
    """
    print(f"{'ID:':<25} {evento.idEvento:<45}")
    print(f"{'ID Organizador:':<25} {evento.idOrganizador:<45}")
    print(f"{'Nome:':<25} {evento.nome:<45}")
    print(f"{'Descrição:':<25} {evento.descricao:<45}")
    print(f"{'Data:':<25} {str(evento.data):<45}")
    print(f"{'Máximo de inscritos:':<25} {evento.numeroMaxParticipantes:<45}")
    print(f"{'Inscritos:':<25} {len(evento.alunosInscritos):<45}")
    print("_-" * 60)

def criar_data()-> date:
    """
    Cria uma data com base nas respostas do usuário

    :return: objeto datetime.date com a data escolhida pelo usuário
    :rtype: date
    """
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    data = date(ano, mes, dia)
    return data

def criar_aluno(usuarios: list) -> object:
    """
    Registra um aluno no sistema
    
    :param usuarios: lista dos usuarios existentes
    :type usuarios: list
    :return: retorna o aluno criado
    :rtype: object
    """

    confirmado = False
    while confirmado != True:
        limpar_terminal()
        try:
            titulo("Criar Conta de Aluno")

            dados = coleta_de_dados_usuarios()
            RA = len(usuarios) + 50000000
            curso = input("Curso: ")
            ano = input("Ano que ingressou na faculdade: ")

            #Criando Usuário
            aluno = Aluno(dados["nome"], dados["dataDeNascimento"], dados["senha"], dados["email"], dados["dataDeCadastro"], RA, curso, int(ano))
            usuarios.append(aluno)
            print("Conta criada com sucesso!")
            sleep(2)
            confirmado = True
        
        except:
            print("informações inválidas!")
            sleep(2)
    
    return aluno

def criar_organizador(usuarios: list) -> object:
    """
        Cria um organizador no sistema

        :param usuarios: lista de usuario cadastrados
        :type usaurios: list
        :return: Retorna o organizador criado
        :rtype: Object
        """
    limpar_terminal()
    confirmado = False
    while confirmado != True:
        try:
            titulo("Criar Conta de Organizador")

            dados = coleta_de_dados_usuarios()
            id_usuario = len(usuarios) + 1

            #Criando Usuário
            organizador = Organizador(dados["nome"], dados["dataDeNascimento"], dados["senha"], dados["email"], dados["dataDeCadastro"], id_usuario)
            usuarios.append(organizador)
            print("Conta criada com sucesso!")
            sleep(2)
            confirmado = True
        
        except:
            print("informações inválidas!")
            sleep(2)
    
    return organizador

def verificaUserType(user: object, organizador = True, aluno = False) -> bool:
    if organizador == True and isinstance(user, Organizador):
        return True
    elif aluno == True and isinstance(user, Aluno):
        return True
    else:
        return False