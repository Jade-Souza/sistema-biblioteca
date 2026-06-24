import unittest

from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

from excecoes import (
    LivroIndisponivelError,
    CadastroDuplicadoError,
    UsuarioInativoError
)


class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.biblioteca = Biblioteca("CEFET")

        self.livro = Livro(
            "L001",
            "1984",
            "George Orwell",
            1949
        )

        self.usuario = Usuario(
            "U001",
            "Ana",
            "ana@email.com"
        )

        self.biblioteca.adicionar_livro(self.livro)
        self.biblioteca.cadastrar_usuario(self.usuario)

    def test_livro_cadastrado(self):
        self.assertEqual(
            len(self.biblioteca.livros),
            1
        )

    def test_usuario_cadastrado(self):
        self.assertEqual(
            len(self.biblioteca.usuarios),
            1
        )

    def test_emprestimo_deixa_livro_indisponivel(self):
        self.biblioteca.emprestar_livro(
            "L001",
            "U001"
        )

        self.assertFalse(
            self.livro.disponivel
        )

    def test_devolucao_deixa_livro_disponivel(self):
        self.biblioteca.emprestar_livro(
            "L001",
            "U001"
        )

        self.biblioteca.devolver_livro(
            "L001"
        )

        self.assertTrue(
            self.livro.disponivel
        )

    def test_emprestar_livro_indisponivel(self):
        self.biblioteca.emprestar_livro(
            "L001",
            "U001"
        )

        with self.assertRaises(
            LivroIndisponivelError
        ):
            self.biblioteca.emprestar_livro(
                "L001",
                "U001"
            )

    def test_cadastro_livro_duplicado(self):
        with self.assertRaises(
            CadastroDuplicadoError
        ):
            self.biblioteca.adicionar_livro(
                Livro(
                    "L001",
                    "Outro Livro",
                    "Autor",
                    2025
                )
            )

    def test_usuario_inativo(self):
        self.usuario.desativar()

        with self.assertRaises(
            UsuarioInativoError
        ):
            self.biblioteca.emprestar_livro(
                "L001",
                "U001"
            )


if __name__ == "__main__":
    unittest.main()