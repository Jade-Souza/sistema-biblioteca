class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True
    
    def descricao(self):
        status = "Disponivel" if self.disponivel else "Emprestado"

        return f"""
Código: {self.codigo}
Título: {self.titulo}
Autor: {self.autor}
Ano: {self.ano}
Status: {status}
"""
    


    