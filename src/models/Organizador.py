from models.Usuario import Usuario
from models.Evento import Evento

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
    
    def criarEvento(self, lista_eventos: list) -> str:
        """
        Cria um evento na lista de eventos
        
        :param lista_eventos: Lista em que ficara os eventos criados
        :type lista_eventos: list
        :return: Retorna a mensagem de evento criado
        :rtype: str
        """
        nome = input("Nome: ")
        print("Data do evento")
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        data = date(ano, mes, dia)
        descricao = input("Descrição: ")
        max_participantes = int(input("Número máximo de participantes: "))

        novo_evento = Evento(len(lista_eventos) + 50000, self._idUsuario, nome, data, descricao, max_participantes)
        lista_eventos.append(novo_evento)

        return "Evento criado com sucesso"

    def cancelarEvento(self, evento: object) -> str:
        """
        Cancela um evento através do próprio objeto Evento
        
        :param evento: Referência do Evento
        :type evento: object Evento
        :return: mensagem do que foi executado ou não
        :rtype: str
        """
        if evento.status == "Ativo":
            evento.status = "Cancelado"
            return "Evento cancelado com sucesso!"
        else:
            return "Imposivel cancelar evento que não esteja Ativo"
    
    def deletarEvento(self, lista_eventos: list, ref_evento: object) -> str:
        """
        Deleta um evento que tenha sido cancelado direto da lista de eventos
        
        :param lista_eventos: Lista com os eventos existentes
        :type lista_eventos: list
        :param ref_evento: Referencia do objeto na lista
        :type ref_evento: object
        :return: Mensagem indicativa do que aconteceu
        :rtype: str
        """
        if ref_evento.status == "Cancelado":
            lista_eventos.remove(ref_evento)
            return "Evento deletado com sucesso!"
        else:
            return "Apenas eventos 'Cancelado' podem ser deletados!"
        