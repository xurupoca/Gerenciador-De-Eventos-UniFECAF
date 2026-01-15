import pytest
from models.Usuario import Usuario
from datetime import date

def test_criando_usuario():
    novo_usuario = Usuario("Jonathan", date(2002, 4, 9), "Manga", "JonathanPoli17@gmail.com", date.today())
    assert novo_usuario.VerificarLogin("JonathanPoli17@gmail.com", "Manga")

def test_erro_ValueError_gerado_ao_criarUsuario():
    with pytest.raises(ValueError):
        novo_usuario = Usuario("1Jona than", date(2002, 4, 9), "Manga", "JonathanPoli17@gmail.com", date.today())
        novo_usuario = Usuario("Jonathan", "2002, 4, 9", "Manga", "JonathanPoli17@gmail.com", date.today())
        novo_usuario = Usuario("Jonathan", date(2002, 4, 9), "Manga 12", "JonathanPoli17@gmail.com", date.today())
        novo_usuario = Usuario("Jonathan", date(2002, 4, 9), "Manga", "Jonatha nPoli17gmail.com", date.today())
        novo_usuario = Usuario("Jonathan", date(2002, 4, 9), "Manga", "JonathanPoli17@gmail.com", "date.today()")