# Classe que representa um livro dentro do sistema de biblioteca
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo        
        self.autor = autor         
        self.isbn = isbn            
        self.disponivel = True      # Define o livro como disponível ao ser criado

    # Método para emprestar o livro
    def emprestar(self):
        if self.disponivel:         # Verifica se o livro está disponível
            self.disponivel = False # Marca como indisponível após o empréstimo
            return True             # Empréstimo bem-sucedido
        return False                # Empréstimo falhou porque o livro já está emprestado

    # Método para devolver o livro
    def devolver(self):
        self.disponivel = True      # Marca o livro como disponível novamente
