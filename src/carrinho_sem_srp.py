# ============================================================
# # CARRINHO DE COMPRAS - SEM SRP
# Tudo em uma única classe
# ============================================================

class CarrinhoCompra:

    # --- Atributos que vamos trabalhar ---
    # itens       : lista de dicionários {"item": str, "valor": float}
    # status      : str  ("aberto" | "confirmado")
    # valor_total : float

    def __init__(self):
        self.itens = []
        self.status = "aberto"
        self.valor_total = 0.0

    # --- Métodos ---

    def exibir_itens(self):
        return self.itens

    def adicionar_item(self, item: str, valor: float) -> bool:
        self.itens.append({"item": item, "valor": valor})
        self.valor_total += valor
        return True

    def exibir_valor_total(self) -> float:
        return self.valor_total

    def exibir_status(self) -> str:
        return self.status

    def validar_carrinho(self) -> bool:
        return len(self.itens) > 0

    def enviar_email_confirmacao(self):
        print(".... envia e-mail de confirmação ....")

    def confirmar_pedido(self) -> bool:
        if self.validar_carrinho():
            self.status = "confirmado"
            self.enviar_email_confirmacao()
            return True
        return False
