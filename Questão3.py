# Classe base Produto
class Produto:
    def __init__(self, codigo: int, descricao: str, valor: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    def exibir_detalhes(self):
        return "Código: {}, Descrição: {}, Valor: R${:.2f}".format(self.codigo, self.descricao, self.valor)

    def imprimir(self):
        print(self.exibir_detalhes())


# Classe Eletronico que herda de Produto
class Eletronico(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, voltagem: int):
        super().__init__(codigo, descricao, valor)
        self.voltagem = voltagem

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Voltagem: {}V".format(self.voltagem)

    def imprimir(self):
        print(self.exibir_detalhes())


# Classe Vestuario que herda de Produto
class Vestuario(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str):
        super().__init__(codigo, descricao, valor)
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Nome: {}, Cor: {}, Tamanho: {}".format(self.nome, self.cor, self.tamanho)

    def imprimir(self):
        print(self.exibir_detalhes())


# Classe Calcado que herda de Vestuario
class Calcado(Vestuario):
    def __init__(
        self,
        codigo: int,
        descricao: str,
        valor: float,
        nome: str,
        cor: str,
        tamanho: str,
        materialsola: str,
        materialpartesuperior: str,
        materialinterno: str,
    ):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.materialsola = materialsola
        self.materialpartesuperior = materialpartesuperior
        self.materialinterno = materialinterno

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Material da Sola: {}, Material Parte Superior: {}, Material Interno: {}".format(
            self.materialsola, self.materialpartesuperior, self.materialinterno
        )

    def imprimir(self):
        print(self.exibir_detalhes())


# Classe Roupa que herda de Vestuario
class Roupa(Vestuario):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str, tecido: str):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.tecido = tecido

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return detalhes + ", Tecido: {}".format(self.tecido)

    def imprimir(self):
        print(self.exibir_detalhes())


# Criação de Objetos e Execução do Método Imprimir

# Objetos da classe Eletronico
eletronico1 = Eletronico(101, "Smartphone", 2500.0, 110)
eletronico2 = Eletronico(102, "Notebook", 4500.0, 220)
eletronico1.imprimir()
eletronico2.imprimir()

# Objetos da classe Calcado
calcado1 = Calcado(201, "Tênis esportivo", 300.0, "Tênis", "Preto", "42", "Borracha", "Tecido sintético", "Espuma")
calcado2 = Calcado(202, "Bota de couro", 450.0, "Bota", "Marrom", "39", "Couro", "Couro", "Lã")
calcado1.imprimir()
calcado2.imprimir()

# Objetos da classe Roupa
roupa1 = Roupa(301, "Camiseta básica", 50.0, "Camiseta", "Branca", "M", "Algodão")
roupa2 = Roupa(302, "Jaqueta de inverno", 350.0, "Jaqueta", "Preta", "G", "Poliéster")
roupa1.imprimir()
roupa2.imprimir()
