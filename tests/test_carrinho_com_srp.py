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


# ============================================================
# TESTES — CarrinhoCompra
# Responsabilidade testada: gerenciar itens e valor total
# ============================================================
 
class TestCarrinhoCompra:
 
    def test_carrinho_inicia_sem_itens(self):
        carrinho = CarrinhoCompra()
        assert carrinho.exibir_itens() == []
 
    def test_carrinho_inicia_com_valor_zero(self):
        carrinho = CarrinhoCompra()
        assert carrinho.exibir_valor_total() == 0.0
 
    def test_adicionar_item_retorna_true(self):
        carrinho = CarrinhoCompra()
        resultado = carrinho.adicionar_item("Bicicleta", 750.10)
        assert resultado == True
 
    def test_adicionar_item_aumenta_lista(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        assert len(carrinho.exibir_itens()) == 1
 
    def test_adicionar_dois_itens_lista_tem_dois(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        carrinho.adicionar_item("Tapete", 350.20)
        assert len(carrinho.exibir_itens()) == 2
 
    def test_valor_total_soma_um_item(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        assert carrinho.exibir_valor_total() == 750.10
 
    def test_valor_total_soma_dois_itens(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        carrinho.adicionar_item("Tapete", 350.20)
        assert round(carrinho.exibir_valor_total(), 2) == 1100.30
 
    def test_exibir_itens_retorna_lista_de_dicionarios(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        itens = carrinho.exibir_itens()
        assert isinstance(itens, list)
        assert isinstance(itens[0], dict)
 
    def test_exibir_itens_contem_nome_correto(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        assert carrinho.exibir_itens()[0]["item"] == "Bicicleta"
 
    def test_get_itens_retorna_objetos_item_carrinho(self):
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        assert isinstance(carrinho.get_itens()[0], ItemCarrinho)


# ============================================================
# TESTES - ValidadorCarrinho
# Responsabilidade testada: validar regras de negócio
# ============================================================
 
class TestValidadorCarrinho:
 
    def test_carrinho_vazio_e_invalido(self):
        # Arrange
        validador = ValidadorCarrinho()
        carrinho = CarrinhoCompra()
        # Act
        resultado = validador.validar(carrinho)
        # Assert
        assert resultado == False
 
    def test_carrinho_com_um_item_e_valido(self):
        validador = ValidadorCarrinho()
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Televisão", 3570.25)
        assert validador.validar(carrinho) == True
 
    def test_carrinho_com_varios_itens_e_valido(self):
        validador = ValidadorCarrinho()
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("Bicicleta", 750.10)
        carrinho.adicionar_item("Geladeira", 1950.15)
        carrinho.adicionar_item("Tapete", 350.20)
        assert validador.validar(carrinho) == True 



# ============================================================
# TESTES - EmailService
# Responsabilidade testada: enviar e-mails
# ============================================================
 
class TestEmailService:
 
    def test_enviar_confirmacao_executa_sem_erro(self):
        # O EmailService só imprime — verificamos que não lança exceção
        email = EmailService()
        try:
            email.enviar_confirmacao()
            executou = True
        except Exception:
            executou = False
        assert executou == True
 
    def test_enviar_confirmacao_imprime_mensagem(self, capsys):
        # capsys é um recurso do pytest que captura o print()
        email = EmailService()
        email.enviar_confirmacao()
        saida = capsys.readouterr().out
        assert "e-mail" in saida


# ============================================================
# TESTES - PedidoService
# Responsabilidade testada: orquestrar a confirmação do pedido
# ============================================================
 
class TestPedidoService:
 
    def test_status_inicial_e_aberto(self):
        pedido = PedidoService()
        assert pedido.exibir_status() == "aberto"
 
    def test_confirmar_pedido_com_itens_retorna_true(self):
        pedido = PedidoService()
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item('Televisão 65"', 3570.25)
        assert pedido.confirmar_pedido(carrinho) == True
 
    def test_confirmar_pedido_sem_itens_retorna_false(self):
        pedido = PedidoService()
        carrinho = CarrinhoCompra()
        assert pedido.confirmar_pedido(carrinho) == False
 
    def test_status_muda_para_confirmado_apos_pedido(self):
        pedido = PedidoService()
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item('Televisão 65"', 3570.25)
        pedido.confirmar_pedido(carrinho)
        assert pedido.exibir_status() == "confirmado"
 
    def test_status_nao_muda_se_carrinho_vazio(self):
        pedido = PedidoService()
        carrinho = CarrinhoCompra()
        pedido.confirmar_pedido(carrinho)
        assert pedido.exibir_status() == "aberto"
 
    def test_dois_pedidos_independentes(self):
        # Cada instância de PedidoService é independente
        pedido1 = PedidoService()
        pedido2 = PedidoService()
        carrinho = CarrinhoCompra()
        carrinho.adicionar_item("TV", 3570.25)
        pedido1.confirmar_pedido(carrinho)
        # pedido2 não confirmou - deve continuar aberto
        assert pedido2.exibir_status() == "aberto"
 