import pandas as pd
#definindo metas para verificação das cores.
meta_faturamento_dia = 1000
meta_diversidadeProduto_dia = 4
meta_ticketMedio_dia = 500
meta_faturamento_ano = 1650000
meta_diversidadeProduto_Ano = 120
meta_ticketMedio_ano = 500
class VerificarCores:

    def __init__(self):
        pass


    def verificar_cor_faturamentoDia(self, faturamento_dia):
        if faturamento_dia >= meta_faturamento_dia:
            cor_faturamento_dia = 'green'
        else:
            cor_faturamento_dia = 'red'
        return cor_faturamento_dia


    def verificar_cor_faturamentoAno(self, faturamento_ano):
        if faturamento_ano >= meta_faturamento_ano:
            cor_faturamento_ano = 'green'
        else:
            cor_faturamento_ano = 'red'
        return cor_faturamento_ano


    def verificar_cor_diversidade_produtoDia(self, diversidade_produto_dia):
        if diversidade_produto_dia >= meta_diversidadeProduto_dia:
            cor_diversidade_produtoDia = 'green'
        else:
            cor_diversidade_produtoDia = 'red'
        return cor_diversidade_produtoDia


    def verificar_cor_diversidade_produtoAno(self, diversidade_produto_ano):
        if diversidade_produto_ano >= meta_diversidadeProduto_Ano:
            cor_diversidade_produtoAno = 'green'
        else:
            cor_diversidade_produtoAno = 'red'
        return cor_diversidade_produtoAno


    def verificar_cor_ticketMedioDia(self, ticket_medio_dia):
        if ticket_medio_dia >= meta_ticketMedio_dia:
            cor_ticketMedio_dia = 'green'
        else:
            cor_ticketMedio_dia = 'red'
        return cor_ticketMedio_dia


    def verificar_cor_ticketMedioAno(self, ticket_medio_ano):
        if ticket_medio_ano >= meta_ticketMedio_ano:
            cor_ticketMedio_ano = 'green'
        else:
            cor_ticketMedio_ano = 'red'
        return cor_ticketMedio_ano

class CriarEmail():
    def __init__(self):
        pass

    def criar_emailHTML_gerentes(self, loja, nome, dia_indicador, faturamento_dia, faturamento_ano, ticket_medio_dia,
                                 ticket_medio_ano, diversidade_produto_dia, diversidade_produto_ano):
        email_text = f'''
        <p>Bom dia, {nome}.</p>

        <p>O resultado de ontem: <strong>({dia_indicador.day}/{dia_indicador.month})</strong> da <strong>loja {loja} </strong> foi:</p>
          ''' + '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
           font-family: arial, sans-serif;
           border-collapse: collapse;
           width: 100%;
        }
    
        td, th {
           border: 1px solid #dddddd;
           text-align: left;
           padding: 8px;
        }
    
         tr:nth-child(even) {
            background-color: #dddddd;
         }
      
      </style>
      </head>
      <body>
      ''' + f'''
      
      <h2>Indicadores de Performance</h2>
    
      <table>
        <table>
        <tr>
          <th style="text-align: center">Indicador</th>
          <th style="text-align: center">Valor Diário</th>
          <th style="text-align: center">Meta Diária</th>
          <th style="text-align: center">Cenário Diário</th>
        </tr>
        <tr>
          <td style="text-align: center">Faturamento</td>
          <td style="text-align: center">R${faturamento_dia:.2f}</td>
          <td style="text-align: center">R${meta_faturamento_dia:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_faturamentoDia(faturamento_dia)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Diversidade de Produto</td>
          <td style="text-align: center">{diversidade_produto_dia}</td>
          <td style="text-align: center">{meta_diversidadeProduto_dia}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_diversidade_produtoDia(diversidade_produto_dia)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Ticket Médio</td>
          <td style="text-align: center">R${ticket_medio_dia:.2f}</td>
          <td style="text-align: center">R${meta_ticketMedio_dia:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_ticketMedioDia(ticket_medio_dia)}">◙</font></td>
        </tr>
        </table>
        <p></p>
        <hr>
        <p></p>
        <table>
        <tr>
          <th style="text-align: center">Indicador</th>
          <th style="text-align: center">Valor Anual</th>
          <th style="text-align: center">Meta Anual</th>
          <th style="text-align: center">Cenário Anual</th>
        </tr>
        <tr>
          <td style="text-align: center">Faturamento</td>
          <td style="text-align: center">R${faturamento_ano:.2f}</td>
          <td style="text-align: center">R${meta_faturamento_ano:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_faturamentoAno(faturamento_ano)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Diversidade de Produto</td>
          <td style="text-align: center">{diversidade_produto_ano}</td>
          <td style="text-align: center">{meta_diversidadeProduto_Ano}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_diversidade_produtoAno(diversidade_produto_ano)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Ticket Médio</td>
          <td style="text-align: center">R${ticket_medio_ano:.2f}</td>
          <td style="text-align: center">R${meta_ticketMedio_ano:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_ticketMedioAno(ticket_medio_ano)}">◙</font></td>
        </tr>
        </table>
      </table>

      </body>
      </html>
      <!DOCTYPE html>
      <html>
      <head>

      </head>
      <body>
      <p></p>
      <p>Segue em anexo a planilha com todos os dados para mais detalhes.<p>
      <p>Qualquer dúvida, fico a disposição.</p>
      <p>Att. Renan D.Leal</p>
      '''
        return email_text
















