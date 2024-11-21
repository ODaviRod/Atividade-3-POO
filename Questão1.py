# Classe base Produto
class Produto:
    def __init__(self, codigo: int, descricao: str, valor: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor


# Classe Eletronico que herda de Produto
class Eletronico(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, voltagem: int):
        super().__init__(codigo, descricao, valor)
        self.voltagem = voltagem


# Classe Vestuario que herda de Produto
class Vestuario(Produto):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str):
        super().__init__(codigo, descricao, valor)
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho


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


# Classe Roupa que herda de Vestuario
class Roupa(Vestuario):
    def __init__(self, codigo: int, descricao: str, valor: float, nome: str, cor: str, tamanho: str, tecido: str):
        super().__init__(codigo, descricao, valor, nome, cor, tamanho)
        self.tecido = tecido
