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


# ------------------------------------------------------------
# 4. EmailService
#    Responsabilidade: enviar e-mails (confirmação, etc.).
# ------------------------------------------------------------
class EmailService:

    def enviar_confirmacao(self):
        print(".... envia e-mail de confirmação ....")



# ------------------------------------------------------------
# 5. PedidoService
#    Responsabilidade: orquestrar a confirmação do pedido,
#    coordenando validação, status e notificação.
# ------------------------------------------------------------
class PedidoService:

    def __init__(self):
        self._status: str = "aberto"
        self._validador = ValidadorCarrinho()
        self._email_service = EmailService()

    def exibir_status(self) -> str:
        return self._status

    def confirmar_pedido(self, carrinho: CarrinhoCompra) -> bool:
        if self._validador.validar(carrinho):
            self._status = "confirmado"
            self._email_service.enviar_confirmacao()
            return True
        return False



# ============================================================
# BLOCO DE EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    carrinho1 = CarrinhoCompra()
    pedido1 = PedidoService()

    print("Itens:", carrinho1.exibir_itens())
    print("Valor total:", carrinho1.exibir_valor_total())

    # Descomente para testar com mais itens:
    # carrinho1.adicionar_item("Bicicleta", 750.10)
    # carrinho1.adicionar_item("Geladeira", 1950.15)
    # carrinho1.adicionar_item("Tapete", 350.20)

    print("Itens:", carrinho1.exibir_itens())
    print("Valor total recalculado:", carrinho1.exibir_valor_total())
    print("Status:", pedido1.exibir_status())

    carrinho1.adicionar_item('Televisão 65"', 3570.25)

    if pedido1.confirmar_pedido(carrinho1):
        print("Pedido realizado com sucesso!")
    else:
        print("Erro na confirmação do pedido. Carrinho não possui itens.")

    print("Status:", pedido1.exibir_status())