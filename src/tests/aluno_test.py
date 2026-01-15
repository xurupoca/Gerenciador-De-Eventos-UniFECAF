from models.Aluno import Aluno

import pytest
from datetime import date

def test_erro_RA_criar_aluno():
    with pytest.raises(ValueError):
        aluno = Aluno("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), "12", "Engenharia", 2020)

def test_erro_anoIngresso_criar_aluno():
    with pytest.raises(ValueError):
        aluno = Aluno("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), 12, "Engenharia", "2022")