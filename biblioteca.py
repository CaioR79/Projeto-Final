# Importa a tipagem List para indicar listas de objetos específicos, as classes Livro do módulo livro.py, Usuario do módulo usuario.py e Emprestimo do módulo emprestimo.py
from typing import List
from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo

# Define a classe principal do sistema: Biblioteca
class Biblioteca:
    # Construtor da classe Biblioteca
    def __init__(self):
        self.livros: List[Livro] = []           # Lista para armazenar objetos do tipo Livro
        self.usuarios: List[Usuario] = []       # Lista para armazenar objetos do tipo Usuario
        self.emprestimos: List[Emprestimo] = [] # Lista para armazenar objetos do tipo Emprestimo

    # Método que busca um usuário pelo seu ID
    def buscar_usuario(self, user_id: str):
        for user in self.usuarios:
            if user_id == user.id:
                return user  # Retorna o usuário se encontrado

    # Método para adicionar um livro à biblioteca
    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)  

    # Método para remover um livro da biblioteca
    def remover_livro(self, livro: Livro):
        self.livros.remove(livro)  

    # Método que busca um livro pelo seu ISBN
    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro  
        return None  

    # Método que registra um empréstimo de um livro a um usuário
    def registrar_emprestimo(self, usuario, livro):
        # Busca o livro atualizado e o usuário pelo ID
        livro = self.buscar_livro(livro.isbn)
        user = self.buscar_usuario(usuario.id)

        # Verifica se ambos existem
        if livro and user:
            # Cria uma nova instância de Emprestimo
            emprestimo = Emprestimo(livro, usuario)
            # Registra a data de empréstimo
            emprestimo.registrar_emprestimo()
            # Adiciona o empréstimo à lista
            self.emprestimos.append(emprestimo)
            return True  # Retorna sucesso

        return False  # Retorna falha se livro ou usuário não forem encontrados

    # Método que registra a devolução de um livro
    def registrar_devolucao(self, usuario, livro):
        for emprestimo in self.emprestimos:
            # Verifica se o empréstimo corresponde ao livro e usuário e se ainda não foi devolvido
            if (
                emprestimo.livro == livro
                and emprestimo.usuario == usuario
                and emprestimo.data_devolucao is None
            ):
                # Registra a devolução e remove o empréstimo da lista
                emprestimo.registrar_devolucao()
                self.emprestimos.remove(emprestimo)
                return  # Sai do método após devolver

        # Se nenhum empréstimo correspondente for encontrado
        print("Empréstimo não encontrado ou livro já devolvido.")
