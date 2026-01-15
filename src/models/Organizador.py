from models.Usuario import Usuario

from datetime import date

class Organizador(Usuario):

    def __init__(self, nome: str, dataDeNascimento: date, senha: str, email: str, dataDeCadastro: date, id_usuario: int):
        super().__init__(nome, dataDeNascimento, senha, email, dataDeCadastro)

        self.idUsuario = id_usuario

    @property
    def idUsuario(self) -> int:
        return self._idUsuario
    
    @idUsuario.setter
    def idUsuario(self, id: int):
        if isinstance(id, int):
            self._idUsuario = id
        else:
            raise ValueError("id_Usuario deve do tipo int")