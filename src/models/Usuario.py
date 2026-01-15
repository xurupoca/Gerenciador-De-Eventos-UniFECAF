from datetime import date

class Usuario:
    def __init__(self, nome: str, dataDeNascimento: date, senha: str, email: str, dataDeCadastro: date):
        self.nome = nome
        self.dataDeNascimento = dataDeNascimento
        self.senha = senha
        self.email = email
        self.dataDeCadastro = dataDeCadastro

    def VerificarLogin(self, email: str, senha: str) -> bool:
        """
        Faz a verificação do login do usuário

        :param email: Email do usuário
        :type email: str
        :param senha: senha do usuário
        :type senha: str
        :return: Retorna True se os dados estiverem corretos
        :rtype: bool
        """
        if email.lower().strip() == self._email:
            if senha == self.senha:
                return True
            
        return False
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        """
        Define as regras para inserção do nome

        :param nome: Nome do usuário
        """
        nome = nome.capitalize().strip()
        if nome.replace(" ", "").isalpha():
            self._nome = nome
        else:
            raise ValueError("Nome deve conter apenas letras")
        
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str):
        """
        Define as regras para inserção do email
        
        :param email: Email do usuario
        :type email: str
        """
        email = email.lower().replace(" ", "")
        if email.count("@") == 1 and "." in email:
            self._email = email
        else:
            raise ValueError("Email fora do padrão")
    
    @property
    def dataDeNascimento(self) -> date:
        return self._dataDeNascimento
    
    @dataDeNascimento.setter
    def dataDeNascimento(self, data: date):
        """
        Define as regras para inserção do dataDeNascimento
        
        :param data: data de nascimento do usuário
        :type data: date
        """
        if type(data) == type(date.today()):
            self._dataDeNascimento = data
        else:
            raise ValueError("Data de Nascimento deve ter o tipo date")
    
    @property
    def dataDeCadastro(self) -> date:
        return self._dataDeCadastro
    
    @dataDeCadastro.setter
    def dataDeCadastro(self, data: date):
        """
        Define as regras para inserção da dataDeCadastro
        
        :param data: data de cadastro do usuário
        :type data: date
        """
        if type(data) == type(date.today()):
            self._dataDeCadastro = data
        else:
            raise ValueError("Data de Cadastro deve ter o tipo date")