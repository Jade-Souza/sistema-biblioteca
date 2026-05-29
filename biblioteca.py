from datetime import date
from emprestimo import Emprestimo


class Biblioteca:

    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        for l in self.livros:

            if l.codigo == livro.codigo:
                print("Erro: já existe livro com esse código.")
                return

        self.livros.append(livro)

        print(f"Livro '{livro.titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario):
        for u in self.usuarios:

            if u.matricula == usuario.matricula:
                print("Erro: já existe usuário com essa matrícula.")
                return

        self.usuarios.append(usuario)

        print(f"Usuário '{usuario.nome}' cadastrado com sucesso!")

    def listar_livros(self):
        print("\n--- LIVROS CADASTRADOS ---")

        for livro in self.livros:

            print(livro.descricao())

    def listar_livros_disponiveis(self):
        print("\n--- LIVROS DISPONÍVEIS ---")

        for livro in self.livros:

            if livro.disponivel:

                print(livro.descricao())

    def buscar_livros_por_titulo(self, titulo):
        print("\n--- BUSCA POR TÍTULO ---")

        for livro in self.livros:

            if titulo.lower() in livro.titulo.lower():

                print(livro.descricao())

    def buscar_livros_por_autor(self, autor):
        print("\n--- BUSCA POR AUTOR ---")

        for livro in self.livros:

            if autor.lower() in livro.autor.lower():

                print(livro.descricao())

    def emprestar_livro(self, codigo_livro, matricula):
        livro = None
        usuario = None

        for l in self.livros:

            if l.codigo == codigo_livro:
                livro = l

        for u in self.usuarios:

            if u.matricula == matricula:
                usuario = u

        if livro is None:
            print("Livro não encontrado.")
            return

        if usuario is None:
            print("Usuário não encontrado.")
            return

        if not livro.disponivel:
            print("Erro: livro indisponível.")
            return

        if not usuario.ativo:
            print("Erro: usuário inativo.")
            return

        livro.emprestar()

        emprestimo = Emprestimo(
            livro,
            usuario,
            str(date.today())
        )

        self.emprestimos.append(emprestimo)

        print(f"Livro '{livro.titulo}' emprestado para {usuario.nome}.")

    def devolver_livro(self, codigo_livro):
        for emprestimo in self.emprestimos:

            if (
                emprestimo.livro.codigo == codigo_livro
                and emprestimo.ativo
            ):

                emprestimo.registrar_devolucao(str(date.today()))

                emprestimo.livro.devolver()

                print(f"Livro '{emprestimo.livro.titulo}' devolvido.")

                return

        print("Nenhum empréstimo ativo encontrado.")

    def listar_emprestimos_ativos(self):
        print("\n--- EMPRÉSTIMOS ATIVOS ---")

        encontrou = False

        for emprestimo in self.emprestimos:

            if emprestimo.ativo:

                encontrou = True

                print(emprestimo.resumo())

        if not encontrou:

            print("Não há empréstimos ativos.")

