import pytest
from models.Evento import Evento
from models.Aluno import Aluno
from datetime import date

def test_evento_id_erro():
    with pytest.raises(TypeError):
        evento = Evento(1.2, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)

def test_criar_evento():
    evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)

def test_alterar_numero_max_participates():
    with pytest.raises(ValueError):
        evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)
        aluno =  Aluno("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), 12, "Engenharia", 2022)
        evento.alunosInscritos.append(aluno)
        evento.numeroMaxParticipantes = 0

def test_exportar_alunos_csv_pdf():
    evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)
    aluno =  Aluno("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), 12, "Engenharia", 2022)
    evento.alunosInscritos.append(aluno)
    evento.exportarListaParticipantes(True, True, "alunos_test")

def test_alterar_status_evento():
    evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)
    evento.status = "Concluido"

def test_erro_status_nao_permitido():
    with pytest.raises(ValueError):
        evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)
        evento.status = "Em Aberto"

def test_listar_participantes():
    evento = Evento(12, 12, "loucura", date(2026, 2, 3), "Evento louco", 120)
    aluno =  Aluno("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), 12, "Engenharia", 2022)
    evento.alunosInscritos.append(aluno)
    evento.listarParticipantes()