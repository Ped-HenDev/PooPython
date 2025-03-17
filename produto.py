class Produto:
    def __init__(self, codigo, nome, descricao, categoria, preco, estoque, perecivel):
        if type(codigo) <=0:
            raise ValueError("Código Inválido! ")
        if type(nome) != str and len(nome) < 2:
            raise ValueError("Nome Inválido! ")
        if type(descricao) != str:
            raise ValueError("Descrição Inválida")
        if type(categoria) != str or categoria not in ["Frutas", "Eletrônicos", "Roupas", "Bebidas"]:
            raise ValueError("Categoria Inválida")
        if type(preco) != float or preco <=0:
            raise ValueError("Preço Inválido!")
        if type(estoque) !=int or estoque <0:
            raise ValueError("Estoque Inválido!")
        if type(perecivel) != bool:
            raise ValueError("Inválido!")

        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.perecivel = perecivel
def reajustar_preco(self, percentual):
    if percentual <=0:
        raise ValueError("Percentual de reajuste Inválido")
    self.preco = self.preco *(1+percentual/100)