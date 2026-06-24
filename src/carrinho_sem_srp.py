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

# ============================================================
# BLOCO DE EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    carrinho1 = CarrinhoCompra()

    print("Itens:", carrinho1.exibir_itens())
    print("Valor total:", carrinho1.exibir_valor_total())

    # Descomenta para testar com mais itens:
    carrinho1.adicionar_item("Bicicleta", 750.10)
    # carrinho1.adicionar_item("Geladeira", 1950.15)
    # carrinho1.adicionar_item("Tapete", 350.20)

    print("Itens:", carrinho1.exibir_itens())
    print("Valor total recalculado:", carrinho1.exibir_valor_total())
    print("Status:", carrinho1.exibir_status())

    carrinho1.adicionar_item('Televisão 65"', 3570.25)

    if carrinho1.confirmar_pedido():
        print("Pedido realizado com sucesso!")
    else:
        print("Erro na confirmação do pedido. Carrinho não possui itens.")

    print("Status:", carrinho1.exibir_status())

# ============================================================
# RESULTADO ESPERADO NO TERMINAL
# ============================================================
#  Cliente pega o carrinho vazio
#        ↓
# Carrinho: []  →  R$ 0,00  →  status: aberto
#        ↓
# Cliente adiciona Televisão 65" por R$ 3.570,25
#        ↓
# Cliente clica em "Finalizar Pedido"
#        ↓
# Sistema valida: tem item? Sim 
#       ↓
# Sistema envia e-mail de confirmação 
#        ↓
# Pedido realizado com sucesso!
#        ↓
# status: confirmado
#
# Tudo isso está acontecendo dentro de uma única classe que faz tudo