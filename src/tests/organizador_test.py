from models.Organizador import Organizador

import pytest
from datetime import date

def test_criar_organizador_erro_id():
    with pytest.raises(ValueError):
        organizador = Organizador("Jonathan", date(2002, 4, 9), "JPloko", "Jonathanpoli17@gmail.com", date(2026, 1, 1), 104.5)