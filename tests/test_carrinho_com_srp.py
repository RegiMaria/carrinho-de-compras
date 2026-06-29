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

 
# ============================================================
# TESTES - ItemCarrinho
# Responsabilidade testada: representar um produto e seu preço
# ============================================================
 
class TestItemCarrinho:
 
    def test_item_guarda_nome_corretamente(self):
        # Arrange
        item = ItemCarrinho("Bicicleta", 750.10)
        # Assert
        assert item.nome == "Bicicleta"
 
    def test_item_guarda_valor_corretamente(self):
        # Arrange
        item = ItemCarrinho("Bicicleta", 750.10)
        # Assert
        assert item.valor == 750.10
 
    def test_to_dict_retorna_dicionario_correto(self):
        # Arrange
        item = ItemCarrinho("Tapete", 350.20)
        # Act
        resultado = item.to_dict()
        # Assert
        assert resultado == {"item": "Tapete", "valor": 350.20}
 
    def test_to_dict_chave_item_existe(self):
        item = ItemCarrinho("Geladeira", 1950.15)
        assert "item" in item.to_dict()
 
    def test_to_dict_chave_valor_existe(self):
        item = ItemCarrinho("Geladeira", 1950.15)
        assert "valor" in item.to_dict()
 