class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):

        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.ativo = True

    def registrar_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao
        self.ativo = False

    def resumo(self):
        status = "Ativo" if self.ativo else "Encerrado"

        return f"""
Livro: {self.livro.titulo}
Usuário: {self.usuario.nome}
Data empréstimo: {self.data_emprestimo}
Data devolução: {self.data_devolucao}
Status: {status}
"""