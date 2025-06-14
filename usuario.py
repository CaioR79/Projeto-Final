# Importa a classe Livro para que o usuário possa interagir com livros
from livro import Livro

# Classe que representa um usuário da biblioteca
class Usuario:
    def __init__(self, nome, id):
        self.nome = nome  
        self.id = id      

    # Método que permite ao usuário tentar emprestar um livro
    def emprestar_livro(self, livro: Livro):
        return livro.emprestar()  # Tenta emprestar o livro e retorna True (sucesso) ou False (falha)

    # Método que permite ao usuário devolver um livro
    def devolver_livro(self, livro: Livro):
        livro.devolver()  # Marca o livro como devolvido (disponível)
