# ============================================================
# TESTES — carrinho_com_srp.py
# Ferramenta: pytest
#
# Para rodar:
#   pip install pytest
#   pytest tests/test_carrinho_com_srp.py -v
#
# Cada classe tem seus próprios testes.
# SRP aplicado
# Também nos testes: cada grupo testa UMA responsabilidade.
# ============================================================
 
import pytest
from src.carrinho_com_srp import (
    ItemCarrinho,
    CarrinhoCompra,
    ValidadorCarrinho,
    EmailService,
    PedidoService,
)
 