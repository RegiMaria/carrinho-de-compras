# ============================================================
# CARRINHO DE COMPRAS - COM SRP (Single Responsibility Principle)
#
# Cada classe deve ter UMA única responsabilidade:
#
#   ItemCarrinho      → representar um produto e seu preço
#   CarrinhoCompra    → gerenciar itens e valor total
#   ValidadorCarrinho → validar o estado do carrinho
#   EmailService      → enviar e-mails de confirmação
#   PedidoService     → orquestrar a confirmação do pedido
#
# ============================================================

# ------------------------------------------------------------
# 1. ItemCarrinho
#    Responsabilidade: representar um produto com seu preço.
# ------------------------------------------------------------
class ItemCarrinho:

    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor

    def to_dict(self) -> dict:
        return {"item": self.nome, "valor": self.valor}


class CarrinhoCompra:

    def __init__(self):
        self.itens: list[ItemCarrinho] = []
        self._valor_total: float = 0.0

    def adicionar_item(self,nome:str, valor:float)  -> bool:
        item = ItemCarrinho(nome,valor)
        self._itens.append(item)
        self._valor_total += valor
        return True
    
    def exibir_itens(self) -> list[dict]:
        return [i.to_dict() for i in self._itens]

    def exibir_valor_total(self) -> float:
        return self._valor_total

    def get_itens(self) -> list[ItemCarrinho]:
        """Retorna a lista interna (usada por outras classes)."""
        return self._itens
    

# ------------------------------------------------------------
# 3. ValidadorCarrinho
#    Responsabilidade: validar regras de negócio do carrinho
# ------------------------------------------------------------
class ValidadorCarrinho:

    def validar(self, carrinho: CarrinhoCompra) -> bool:
        """Retorna True se o carrinho possui pelo menos 1 item."""
        return len(carrinho.get_itens()) > 0

