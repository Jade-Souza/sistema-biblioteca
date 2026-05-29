class Usuario:
    def __init__(self, matricula, nome, email):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.ativo = True

    def ativar(self):
        self.ativo = True
    
    def desativar(self):
        self.ativo = False
    
    def descricao(self):
        status = "Ativo" if self.ativo else "Inativo"

        return f"""
Matrícula: {self.matricula}
Nome: {self.nome}
Email: {self.email}
Status: {status}
"""
    

        

    