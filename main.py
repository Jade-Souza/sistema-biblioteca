from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca

# Importação das exceções personalizadas
from excecoes import (
    LivroIndisponivelError,
    UsuarioInativoError,
    CadastroDuplicadoError,
    LivroNaoEncontradoError,
    UsuarioNaoEncontradoError
)

# CRIAÇÃO DA BIBLIOTECA
biblioteca = Biblioteca("Biblioteca CEFET")


# CRIAÇÃO DOS LIVROS
livro1 = Livro("L001", "Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("L002", "1984", "George Orwell", 1949)
livro3 = Livro("L003", "Python Fluente", "Luciano Ramalho", 2015)


# CRIAÇÃO DOS USUÁRIOS
usuario1 = Usuario("U001", "Ana Souza", "ana@email.com")
usuario2 = Usuario("U002", "Bruno Lima", "bruno@email.com")


# CADASTRO DOS LIVROS E USUÁRIOS
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)


# TESTE 1 - USUÁRIO INATIVO
usuario2.desativar()

try:
    biblioteca.emprestar_livro("L002", "U002")
except UsuarioInativoError as erro:
    print(f"Erro capturado: {erro}")


# LISTAGEM E BUSCAS
print("\n=== LISTA DE LIVROS ===")
biblioteca.listar_livros()

print("\n=== BUSCA POR TÍTULO ===")
biblioteca.buscar_livros_por_titulo("1984")

print("\n=== BUSCA POR AUTOR ===")
biblioteca.buscar_livros_por_autor("Machado")


# EMPRÉSTIMO VÁLIDO
print("\n=== EMPRÉSTIMO VÁLIDO ===")
biblioteca.emprestar_livro("L001", "U001")


# TESTE 2 - LIVRO INDISPONÍVEL
usuario2.ativo = True

try:
    biblioteca.emprestar_livro("L001", "U002")
except LivroIndisponivelError as erro:
    print(f"Erro capturado: {erro}")


# TESTE 3 - CADASTRO DUPLICADO
try:
    biblioteca.adicionar_livro(
        Livro("L001", "Livro Repetido", "Autor Teste", 2026)
    )
except CadastroDuplicadoError as erro:
    print(f"Erro capturado: {erro}")


# LISTAGEM DE EMPRÉSTIMOS ATIVOS
print("\n=== EMPRÉSTIMOS ATIVOS ===")
biblioteca.listar_emprestimos_ativos()


# DEVOLUÇÃO DO LIVRO
print("\n=== DEVOLUÇÃO ===")
biblioteca.devolver_livro("L001")


# LIVROS DISPONÍVEIS
print("\n=== LIVROS DISPONÍVEIS ===")
biblioteca.listar_livros_disponiveis()


# EMPRÉSTIMOS APÓS DEVOLUÇÃO
print("\n=== EMPRÉSTIMOS ATIVOS APÓS DEVOLUÇÃO ===")
biblioteca.listar_emprestimos_ativos()