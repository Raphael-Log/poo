from autor import Autor

def main():
    autor1 = Autor ('Antonio Neto', 1982, 'Rua Tal')
    autor2 = Autor ('Carlos Braga', 1992, 'Rua Total')
    print(autor1._nome)
    print(autor2.calcula_idade(2023))

if __name__ == "_main_":
    main()
