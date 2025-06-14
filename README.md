# Programação Orientada a Maquinas Virtuais

## Sistema Organizacional para Biblioteca

#### Tema: Um sistema para gerenciar livros em uma biblioteca, incluindo funcionalidades para adicionar, remover e pesquisar livros, bem como para realizar o empréstimo e a devolução de livros.

##### Motivação: Muitas bibliotecas precisam de um sistema eficaz para gerenciar seu acervo, rastrear livros emprestados e devolvidos, e garantir que a operação seja eficiente. Este sistema permitirá a automação e a melhoria na organização das operações da biblioteca.

#### Esboço da Solução

Modelagem UML:

- Classe Livro: Representa um livro na biblioteca.

```diff
+---------------------+
|     Livro           |
+---------------------+
| - titulo: str       |
| - autor: str        |
| - isbn: str         |
| - disponivel: bool  |
+---------------------+
| + emprestar(): bool |
| + devolver(): void  |
+---------------------+
```

- Classe Usuario: Representa um usuário da biblioteca.

```diff
+---------------------------------------+
|    Usuario                            |
+---------------------------------------+
| - nome: str                           |
| - id: int                             |
+---------------------------------------+
| + emprestar_livro(livro: Livro): bool |
| + devolver_livro(livro: Livro): void  |
+---------------------------------------+
```

- Classe Emprestimo: Gerencia o empréstimo de livros.

```diff
+---------------------------------+
|   Emprestimo                    |
+---------------------------------+
| - livro: Livro                  |
| - usuario: Usuario              |
| - data_emprestimo: datetime     |
| - data_devolucao: datetime      |
+---------------------------------+
| + registrar_emprestimo(): void  |
| + registrar_devolucao(): void   |
+---------------------------------+
```

- Classe Biblioteca: Coordena os livros e os empréstimos.

```diff
+-----------------+
|   Biblioteca    |
+-----------------+
| - livros: List[Livro] |
| - usuarios: List[Usuario] |
| - emprestimos: List[Emprestimo] |
+-----------------+
| + adicionar_livro(livro: Livro): void |
| + remover_livro(livro: Livro): void   |
| + buscar_livro(isbn: str): Livro |
| + registrar_emprestimo(usuario: Usuario, livro: Livro): bool |
| + registrar_devolucao(usuario: Usuario, livro: Livro): void |
+-----------------+
```