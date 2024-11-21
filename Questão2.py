# Classe base Produto
class Produto:
    def __init__(self, codigo: int, descricao: str, valor: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor

    def exibir_detalhes(self):
        return f"Código: {self.codigo}, Descrição: {self.descricao}, Valor: R${self.valor:.2f}"


# Classe Eletronico que herda de Produto
class Eletronico(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, voltagem: int):
        super().__init__(codigo, descricao, valor)
        self.voltagem = voltagem

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}, Voltagem: {self.voltagem}V"


# Classe Vestuario que herda de Produto
class Vestuario(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str):
        super().__init__(codigo, descricao, valor)
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}, Nome: {self.nome}, Cor: {self.cor}, Tamanho: {self.tamanho}"


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
        return (
            f"{detalhes}, Material da Sola: {self.materialsola}, "
            f"Material Parte Superior: {self.materialpartesuperior}, Material Interno: {self.materialinterno}"
        )


# Classe Roupa que herda de Vestuario
class Roupa(Vestuario):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str, tecido: str):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.tecido = tecido

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}, Tecido: {self.tecido}"


# Criação de Objetos e Execução de Métodos

# Objetos da classe Eletronico
eletronico1 = Eletronico(101, "Smartphone", 2500.0, 110)
eletronico2 = Eletronico(102, "Notebook", 4500.0, 220)
print(eletronico1.exibir_detalhes())
print(eletronico2.exibir_detalhes())

# Objetos da classe Calcado
calcado1 = Calcado(201, "Tênis esportivo", 300.0, "Tênis", "Preto", "42", "Borracha", "Tecido sintético", "Espuma")
calcado2 = Calcado(202, "Bota de couro", 450.0, "Bota", "Marrom", "39", "Couro", "Couro", "Lã")
print(calcado1.exibir_detalhes())
print(calcado2.exibir_detalhes())

# Objetos da classe Roupa
roupa1 = Roupa(301, "Camiseta básica", 50.0, "Camiseta", "Branca", "M", "Algodão")
roupa2 = Roupa(302, "Jaqueta de inverno", 350.0, "Jaqueta", "Preta", "G", "Poliéster")
print(roupa1.exibir_detalhes())
print(roupa2.exibir_detalhes())
