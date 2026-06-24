"""
index.py - Servidor local para o projeto Carrinho de Compras
Execute com:  python index.py
Acesse em:   http://localhost:8000
"""

import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import StringIO

# Adiciona a pasta src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from carrinho_sem_srp import CarrinhoCompra as CarrinhoSemSRP


# ============================================================
# Lógica do carrinho SEM SRP
# ============================================================
def executar_sem_srp():
    saida = []

    carrinho1 = CarrinhoSemSRP()
    saida.append(f"<b>Itens:</b> {carrinho1.exibir_itens()}")
    saida.append(f"<b>Valor total:</b> {carrinho1.exibir_valor_total()}")

    carrinho1.adicionar_item("Bicicleta", 750.10)
    carrinho1.adicionar_item("Geladeira", 1950.15)
    carrinho1.adicionar_item("Tapete", 350.20)

    saida.append(f"<b>Itens:</b> {carrinho1.exibir_itens()}")
    saida.append(f"<b>Valor total recalculado:</b> R$ {carrinho1.exibir_valor_total():.2f}")
    saida.append(f"<b>Status:</b> {carrinho1.exibir_status()}")

    carrinho1.adicionar_item('Televisão 65"', 3570.25)

    if carrinho1.confirmar_pedido():
        saida.append("<b>Pedido realizado com sucesso!</b>")
    else:
        saida.append("<b>Erro na confirmação. Carrinho não possui itens.</b>")

    saida.append(f"<b>Status:</b> {carrinho1.exibir_status()}")
    saida.append(f"<b>Valor total final:</b> R$ {carrinho1.exibir_valor_total():.2f}")

    return "<br>".join(saida)


# ============================================================
# HTML da página
# ============================================================
def gerar_html():
    # Captura o print do enviar_email_confirmacao
    old_stdout = sys.stdout
    sys.stdout = buffer = StringIO()
    resultado = executar_sem_srp()
    sys.stdout = old_stdout
    email_log = buffer.getvalue().replace("\n", "<br>")

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Carrinho de Compras - Sem SRP</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f0f2f5;
            margin: 0;
            padding: 40px;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }}
        .card {{
            background: white;
            border-radius: 10px;
            padding: 30px;
            max-width: 600px;
            margin: 0 auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-top: 5px solid #e74c3c;
        }}
        .card h2 {{
            color: #e74c3c;
            margin-top: 0;
            padding-bottom: 10px;
            border-bottom: 2px solid #eee;
        }}
        .badge {{
            display: inline-block;
            font-size: 0.75em;
            padding: 3px 10px;
            border-radius: 20px;
            background: #e74c3c;
            color: white;
            margin-left: 8px;
            vertical-align: middle;
        }}
        .output {{
            background: #f8f9fa;
            border-left: 4px solid #e74c3c;
            padding: 15px 20px;
            border-radius: 5px;
            line-height: 2.2;
            font-size: 0.95em;
        }}
        .email-log {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 10px 15px;
            border-radius: 5px;
            margin-top: 15px;
            font-size: 0.9em;
            color: #856404;
        }}
        .fluxo {{
            background: #f8f9fa;
            border-left: 4px solid #aaa;
            padding: 15px 20px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 0.88em;
            color: #555;
            line-height: 2;
        }}
        .fluxo b {{
            color: #2c3e50;
        }}
        footer {{
            text-align: center;
            margin-top: 30px;
            color: #aaa;
            font-size: 0.85em;
        }}
    </style>
</head>
<body>
    <h1>🛒 Carrinho de Compras — Padrão SOLID</h1>

    <div class="card">
        <h2>
            Sem SRP
            <span class="badge">1 classe faz tudo</span>
        </h2>

        <div class="output">{resultado}</div>

        {f'<div class="email-log">📧 Log de saída: {email_log}</div>' if email_log.strip() else ''}

        <div class="fluxo">
            <b>Fluxo do carrinho:</b><br>
            Cliente pega o carrinho vazio<br>
            ↓ Carrinho: [] → R$ 0,00 → status: aberto<br>
            ↓ Cliente adiciona itens<br>
            ↓ Cliente clica em "Finalizar Pedido"<br>
            ↓ Sistema valida: tem item? Sim <br>
            ↓ Sistema envia e-mail de confirmação <br>
            ↓ Pedido realizado com sucesso!<br>
            ↓ status: confirmado<br><br>
            ⚠️ <b>Tudo isso dentro de uma única classe - problema do SRP!</b>
        </div>
    </div>

    <footer>Estudo de Padrões SOLID - SRP - Single Responsibility Principle</footer>
</body>
</html>"""


# ============================================================
# Servidor HTTP
# ============================================================
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        html = gerar_html().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Servidor rodando em http://{HOST}:{PORT}")
    print("   Pressione Ctrl+C para encerrar.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n Servidor encerrado.")