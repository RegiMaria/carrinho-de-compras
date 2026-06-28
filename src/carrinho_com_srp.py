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

