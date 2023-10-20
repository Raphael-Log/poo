class Autor:
    def __init__(self, nome, ano_nascimento, endereco):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        self. _endereco = endereco


    def calcula_idade(self, ano_atual):
        idade = ano_atual - self._ano_nascimento
        return idade


class Livro:
     def __init__(self, titulo, ano, valor, autor):
         self._titulo = titulo
         self._ano = ano
         self._valor = valor
         self._autor = Autor