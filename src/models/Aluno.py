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