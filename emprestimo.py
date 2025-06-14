# Importa a biblioteca datetime para trabalhar com datas e horários
from datetime import datetime

# Importa as classes Livro e Usuario necessárias para o empréstimo
from livro import Livro
from usuario import Usuario

# Classe que representa um empréstimo de livro feito por um usuário
class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro  # Referência ao livro emprestado
        self.usuario = usuario  # Referência ao usuário que está pegando o livro
        self.data_emprestimo = datetime.now()  # Data e hora atuais no momento do empréstimo
        self.data_devolucao = None  # Data de devolução inicialmente indefinida (nenhuma)

    # Registra o empréstimo do livro, verificando se está disponível
    def registrar_emprestimo(self):
        if self.livro.emprestar():  # Se o livro está disponível para empréstimo
            print(f"Livro '{self.livro.titulo}' emprestado para {self.usuario.nome}.")
        else:  # Se o livro não estiver disponível
            print(f"Livro '{self.livro.titulo}' não está disponível.")

    # Registra a devolução do livro
    def registrar_devolucao(self):
        self.livro.devolver()  # Chama o método para marcar o livro como devolvido
        self.data_devolucao = datetime.now()  # Registra o momento da devolução
        print(f"Livro '{self.livro.titulo}' devolvido por {self.usuario.nome}.")
