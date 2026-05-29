from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca("Biblioteca CEFET")

# Criando livros
livro1 = Livro("L001", "Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("L002", "1984", "George Orwell", 1949)
livro3 = Livro("L003", "Python Fluente", "Luciano Ramalho", 2015)

# Criando usuários
usuario1 = Usuario("U001", "Ana Souza", "ana@email.com")
usuario2 = Usuario("U002", "Bruno Lima", "bruno@email.com")

# Cadastro
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.cadastrar_usuario(usuario1)
biblioteca.cadastrar_usuario(usuario2)

# Listagem
biblioteca.listar_livros()

# Busca
biblioteca.buscar_livros_por_titulo("1984")
biblioteca.buscar_livros_por_autor("Machado")

# Empréstimo válido
biblioteca.emprestar_livro("L001", "U001")

# Tentativa inválida
biblioteca.emprestar_livro("L001", "U002")

# Empréstimos ativos
biblioteca.listar_emprestimos_ativos()

# Devolução
biblioteca.devolver_livro("L001")

# Livros disponíveis
biblioteca.listar_livros_disponiveis()

# Empréstimos ativos após devolução
biblioteca.listar_emprestimos_ativos()