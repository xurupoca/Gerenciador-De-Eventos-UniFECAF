from datetime import date


class Evento:
    def __init__(self, idEvento: int, idOrganizador: int, nome: str, data: date, descricao: str, numeroMaxParticipantes: int):
        self.idEvento = idEvento
        self.idOrganizador = idOrganizador
        self.nome = nome
        self.data = data
        self.descricao = descricao
        self.alunosInscritos = []
        self.numeroMaxParticipantes = numeroMaxParticipantes
        self.avaliacoes = []
        self.status = "Ativo"


    @property
    def idEvento(self) -> int:
        return self._idEvento
    
    @idEvento.setter
    def idEvento(self, id:int):
        if isinstance(id, int):
            self._idEvento = id
        else:
            raise TypeError("idEvento deve ser do tipo int")
    
    @property
    def idOrganiador(self) -> int:
        return self._idOrganizador
    
    @idOrganiador.setter
    def idOrganizador(self, id: int):
        if isinstance(id, int):
            self._idOrganizador = id
        else:
            raise TypeError("idOrganizador deve ser do tipo int")
        
    @property
    def data(self) -> date:
        return self._data
    
    @data.setter
    def data(self, data_evento: date):
        if data_evento > date.today():
            self._data = data_evento
        else:
            raise ValueError("A data do evento deve ser date e maior do que a data atual")
        
    @property
    def numeroMaxParticipantes(self) -> int:
        return self._numeroMaxParticipantes
    
    @numeroMaxParticipantes.setter
    def numeroMaxParticipantes(self, numero: int):
        if isinstance(numero, int) and numero >= len(self.alunosInscritos):
            self._numeroMaxParticipantes = numero

        else:
            raise ValueError("O número máximo de participantes deve ser int e maior ou igual o total de alunos inscritos")
        
    @property
    def status(self) -> str:
        return self._status
    @status.setter
    def status(self, novo_status: str):
        """
        Controla o status do evento

        :param novo_status: Aceita apenas "Ativo", "Cancelado" ou "Concluido"
        :type novo_status: str
        """
        possiveis_status = ("Ativo", "Cancelado", "Concluido")
        if novo_status in possiveis_status:
            self._status = novo_status
        else:
            raise ValueError("Unicos status possíveis: 'Ativo', 'Cancelado', 'Concluido'")

    def listarParticipantes(self):
        """
        Lista os participantes do Evento
        """
        from utils import titulo
        titulo(f"Participantes do Evento {self.nome}")
        for aluno in self.alunosInscritos:
            print(aluno.RA)
            print(aluno.nome)
            print("_-" * 60)
            print()
        
    def exportarListaParticipantes(self, csv=True, pdf=False, file_name="alunos"):
        """
        Exporta a lista de alunos que vão participar

        :param csv: Tipo de exportação
        :type csv: bool
        :param pdf: Tipo de exportação
        :type pdf: bool
        :param file_name: Nome do arquivo a ser gerado
        :type file_name: str
        """
        data = [
            ["Nome:", self.nome, "Data do Evento:", self._data],
            ["ID do evento:", self.idEvento, "ID do Organizador:", self.idOrganiador],
            [],
            ["RA", "NOME DO ALUNO"]
            ]
        for aluno in self.alunosInscritos:
            data.append([aluno.RA, aluno.nome])
        
        if csv:
            from utils import csv_export
            csv_export(data, file_name)
        if pdf:
            from utils import pdf_export
            pdf_export(data, file_name)