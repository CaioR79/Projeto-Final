# Importa as classes Biblioteca do módulo biblioteca.py, Usuario do módulo usuario.py e Livro do módulo livro.py
from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro


# Define uma função para cadastrar um novo usuário na biblioteca
def cadastrar_usuario(biblioteca: Biblioteca):
    # Solicita o nome do usuário via terminal
    nome = input("Digite o nome do usuario: ")

    # Gera um ID automaticamente com base na quantidade atual de usuários
    id = str(len(biblioteca.usuarios) + 1)

    # Cria uma instância da classe Usuario com o nome e id obtidos
    user = Usuario(nome=nome, id=id)

    # Adiciona o novo usuário à lista de usuários da biblioteca
    biblioteca.usuarios.append(user)

    # Confirma o cadastro do usuário
    print(f'Usuario: {nome} cadastrado com id: {id}')


# Define uma função para cadastrar um novo livro, contendo título, autor e código ISBN
def cadastrar_livro(biblioteca: Biblioteca):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    isbn = input("Digite o isbn do livro: ")

    # Cria uma instância de Livro com os dados fornecidos
    liv = Livro(titulo=titulo, autor=autor, isbn=isbn)
    # Adiciona o livro à coleção da biblioteca (através de um método próprio)
    biblioteca.adicionar_livro(liv)
    # Confirma o cadastro
    print(f'Livro: {titulo} cadastrado com sucesso')

# Define uma função para realizar o empréstimo de um livro
def emprestar_livro(biblioteca: Biblioteca):
    # Solicita o ID do usuário que deseja emprestar
    user_id = input('Digite o id do usuario: ')
    # Busca o usuário pelo ID na lista da biblioteca
    user = biblioteca.buscar_usuario(user_id)
    # Se o usuário não for encontrado, exibe mensagem e encerra a função
    if user is None:
        print(f"Usuario {user_id} nao encontrado")
        return
    
    # Solicita o ISBN do livro a ser emprestado
    isbn = input('Digite o isbn do livro: ')
    
    # Busca o livro pelo ISBN
    livro = biblioteca.buscar_livro(isbn)
    
    # Se o livro não for encontrado, informa ao usuário
    if livro is None:
        print('Livro nao encontrado')

    # Registra o empréstimo (mesmo se o livro for None, o método pode lidar com isso)
    biblioteca.registrar_emprestimo(user, livro)


# Define uma função para registrar a devolução de um livro
def devolver_livro(biblioteca: Biblioteca):
    # Solicita o ID do usuário que está devolvendo
    user_id = input('Digite o id do usuario: ')
    
    # Busca o usuário na base de dados
    user = biblioteca.buscar_usuario(user_id)
    
    # Se não encontrado, exibe erro e encerra
    if user is None:
        print(f"Usuario {user_id} nao encontrado")
        return
    
    # Solicita o ISBN do livro que será devolvido
    isbn = input('Digite o isbn do livro: ')
    
    # Busca o livro na coleção
    livro = biblioteca.buscar_livro(isbn)
    
    # Se o livro não for encontrado, informa ao usuário
    if livro is None:
        print('Livro nao encontrado')

    # Registra a devolução (o método interno deve tratar casos inválidos)
    biblioteca.registrar_devolucao(user, livro)

# Função principal que realiza o funcionamento do sistema
def main():
    # Cria uma instância da classe Biblioteca
    biblioteca = Biblioteca()

    # Dicionário que mapeia opções do menu para funções correspondentes
    choices = {
        '1': cadastrar_usuario,
        '2': cadastrar_livro,
        '3': emprestar_livro,
        '4': devolver_livro
    }
    
    # Loop principal do sistema
    while True:
        # Exibe o menu de opções
        print("\n*****Sistema Organizacional para Biblioteca*****\n")
        print("Selecione a função: ")
        print("1 - Cadastrar usuario")
        print("2 - Cadastrar livro")
        print("3 - Emprestar livro")
        print('4 - Devolver livro')

        # Solicita a opção do usuário
        choice = input("opcao: ")
        
        # Tenta obter a função correspondente à opção digitada
        func = choices.get(choice, None)
        
        # Se a opção for válida, chama a função correspondente
        if func:
            func(biblioteca)
        else:
            # Caso contrário, informa erro de opção inválida
            print('Opcao invalida')


# Este bloco é executado apenas se o script for rodado diretamente
if __name__ == '__main__':
    main()
