from flask import Flask
from Main import indicadores_lojas



app = Flask(__name__)


@app.route("/")  # decorator -> diz em ql link a função vai rodar
def exibir_mensagem():
    mensagem_inicial = "BEM VINDO A API DE CONSUMO DOS INDICADORES DA EMPRESA !!!"
    return f"Mensagem Inicial: {mensagem_inicial}"


@app.route("/indicadores/lojas")
def exibir_indicadores_lojas():
    return indicadores_lojas


@app.route("/indicadores/lojas/faturamento/diario")
def exibir_faturamento_diario_lojas():
    faturamento_diario_lojas = {}
    for loja in indicadores_lojas:
        faturamento_diario_lojas[loja] = indicadores_lojas[loja][0]
    return faturamento_diario_lojas


@app.route("/indicadores/lojas/faturamento/anual")
def exibir_faturamento_anual_lojas():
    faturamento_anual_lojas = {}
    for loja in indicadores_lojas:
        faturamento_anual_lojas[loja] = indicadores_lojas[loja][1]
    return faturamento_anual_lojas


@app.route("/indicadores/lojas/ticketMedio/diario")
def exibir_ticketMedio_diario_lojas():
    ticketMedio_diario_lojas = {}
    for loja in indicadores_lojas:
        ticketMedio_diario_lojas[loja] = indicadores_lojas[loja][2]
    return ticketMedio_diario_lojas


@app.route("/indicadores/lojas/ticketMedio/anual")
def exibir_ticketMedio_anual_lojas():
    ticketMedio_anual_lojas = {}
    for loja in indicadores_lojas:
        ticketMedio_anual_lojas[loja] = indicadores_lojas[loja][3]
    return ticketMedio_anual_lojas


@app.route("/indicadores/lojas/diversidadeProduto/diario")
def exibir_diversidadeProduto_diario_lojas():
    diversidadeProduto_diario_lojas = {}
    for loja in indicadores_lojas:
        diversidadeProduto_diario_lojas[loja] = indicadores_lojas[loja][4]
    return diversidadeProduto_diario_lojas


@app.route("/indicadores/lojas/diversidadeProduto/anual")
def exibir_diversidadeProduto_anual_lojas():
    exibir_diversidadeProduto_anual_lojas = {}
    for loja in indicadores_lojas:
        exibir_diversidadeProduto_anual_lojas[loja] = indicadores_lojas[loja][5]
    return exibir_diversidadeProduto_anual_lojas


@app.route("/indicadores/lojas/<nome_loja>")
def exibir_loja_procurada(nome_loja):
    loja_procurada = {}
    for loja in indicadores_lojas:
        if nome_loja.casefold() == loja.casefold():
            loja_procurada[loja] = indicadores_lojas[loja]
            return loja_procurada


@app.route("/indicadores/lojas/faturamento/total")
def exibir_faturamento_total_empresa():
    faturamento_total = 0
    for loja in indicadores_lojas:
        faturamento_total += indicadores_lojas[loja][1]
    return f"Faturamento Total: {faturamento_total}"


app.run()