import os
import platform
from datetime import date
from time import sleep

from models.Organizador import Organizador
from models.Aluno import Aluno

def titulo(titulo: str):
    if isinstance(titulo, str):
        print("_-" * 60)
        print(f"{titulo:^120}")
        print("_-" * 60)
        print()

    else:
        raise ValueError("título deve ser str")

def limpar_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:  # Linux e macOS
        os.system("clear")

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
        else:
            print("Dados inválidos!")
            sleep(2)
            return None