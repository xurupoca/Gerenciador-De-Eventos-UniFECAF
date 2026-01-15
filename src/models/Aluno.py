from models.Usuario import Usuario

from datetime import date

class Aluno(Usuario):

    def __init__(self, nome: str, dataDeNascimento: date, senha: str, email: str, dataDeCadastro: date, RA: int, curso: str, anoIngresso: int):
        super().__init__(nome, dataDeNascimento, senha, email, dataDeCadastro)

        self.RA = RA
        self.curso = curso
        self.anoIngresso = anoIngresso

    @property
    def RA(self) -> int:
        return self._RA

    @RA.setter
    def RA(self, ra: int):
        if isinstance(ra, int):
            self._RA = ra
        else:
            raise ValueError("RA deve ser int")
    
    @property
    def anoIngresso(self) -> int:
        return self.anoIngresso
    
    @anoIngresso.setter
    def anoIngresso(self, ano: int):
        if isinstance(ano, int) and ano >= 1000 and ano <= 9999:
            self._anoIngresso = ano
        else:
            raise ValueError("O anoIngresso deve ter 4 números do tipo int")
    
    def inscreverseNoEvento(self, evento: object) -> str:
        """
        Inscreve o aluno em um evento
        
        :param evento: Evento em que o aluno quer inscrever-se
        :type evento: object Evento
        :return:  mensagem de confirmação ou negação
        :rtype: str
        """

        msg = ""

        for aluno in evento.alunosInscritos:
            if aluno.RA == self._RA:
                msg = "Aluno já inscrito!"
                return msg

        if evento.status == "Ativo":
            evento.alunosInscritos.append(self)
            msg = "Inscrição realizada!"
        else:
            msg = "Evento não está Ativo!"
        
        return msg

    def desinscreverseNoEvento(self, evento: object) -> str:
        """
        Remove a inscrição do aluno em um evento
        
        :param evento: Evento que deseja remover a inscrição
        :type evento: object Evento
        :return: Mensagem indicativo do que aconteceu
        :rtype: str
        """
        for aluno in evento.alunosInscritos:
            if aluno.RA == self._RA and evento.status == "Ativo":
                evento.alunosInscritos.remove(aluno)
                return "Inscrição removida com sucesso!"
            
        return "Você não está inscrito neste evento!" if evento.status == "Ativo" else "Permitido cancelar inscrição apenas em eventos Ativos!"