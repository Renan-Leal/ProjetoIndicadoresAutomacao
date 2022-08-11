#definindo metas para verificação das cores.
import win32com.client as win32



class VerificarCores:

    def __init__(self):
        self.meta_faturamento_dia = 1000
        self.meta_diversidadeProduto_dia = 4
        self.meta_ticketMedio_dia = 500
        self.meta_faturamento_ano = 1650000
        self.meta_diversidadeProduto_ano = 120
        self.meta_ticketMedio_ano = 500


    def verificar_cor_faturamentoDia(self, faturamento_dia):
        if faturamento_dia >= self.meta_faturamento_dia:
            cor_faturamento_dia = 'green'
        else:
            cor_faturamento_dia = 'red'
        return cor_faturamento_dia


    def verificar_cor_faturamentoAno(self, faturamento_ano):
        if faturamento_ano >= self.meta_faturamento_ano:
            cor_faturamento_ano = 'green'
        else:
            cor_faturamento_ano = 'red'
        return cor_faturamento_ano


    def verificar_cor_diversidade_produtoDia(self, diversidade_produto_dia):
        if diversidade_produto_dia >= self.meta_diversidadeProduto_dia:
            cor_diversidade_produtoDia = 'green'
        else:
            cor_diversidade_produtoDia = 'red'
        return cor_diversidade_produtoDia


    def verificar_cor_diversidade_produtoAno(self, diversidade_produto_ano):
        if diversidade_produto_ano >= self.meta_diversidadeProduto_ano:
            cor_diversidade_produtoAno = 'green'
        else:
            cor_diversidade_produtoAno = 'red'
        return cor_diversidade_produtoAno


    def verificar_cor_ticketMedioDia(self, ticket_medio_dia):
        if ticket_medio_dia >= self.meta_ticketMedio_dia:
            cor_ticketMedio_dia = 'green'
        else:
            cor_ticketMedio_dia = 'red'
        return cor_ticketMedio_dia


    def verificar_cor_ticketMedioAno(self, ticket_medio_ano):
        if ticket_medio_ano >= self.meta_ticketMedio_ano:
            cor_ticketMedio_ano = 'green'
        else:
            cor_ticketMedio_ano = 'red'
        return cor_ticketMedio_ano


class CriarEmail():

    def __init__(self, loja, nome, dia_indicador, faturamento_dia, faturamento_ano, ticket_medio_dia,
                                 ticket_medio_ano, diversidade_produto_dia, diversidade_produto_ano):
        self.loja = loja
        self.nome = nome
        self.dia_indicador = dia_indicador
        self.faturamento_dia = faturamento_dia
        self.faturamento_ano = faturamento_ano
        self.ticket_medio_dia = ticket_medio_dia
        self.ticket_medio_ano = ticket_medio_ano
        self.diversidade_produto_dia = diversidade_produto_dia
        self.diversidade_produto_ano = diversidade_produto_ano


    def criar_email_gerencia(self):
        email_text = f'''
        <p>Bom dia, {self.nome}.</p>

        <p>O resultado de ontem: <strong>({self.dia_indicador.day}/{self.dia_indicador.month})</strong> da <strong>loja {self.loja} </strong> foi:</p>
          ''' + '''
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        table {
           font-family: arial, sans-serif;
           border-collapse: 1px solid black;
           width: 100%;
        }
    
        td, th {
           border: 1px solid #c8c8c8;
           text-align: left;
           padding: 8px;
        }
    
         tr:nth-child(even) {
            background-color: #aee3e6;
         }
      
      </style>
      </head>
      <body>
      ''' + f'''
      
      <h2 style="text-align: center">Indicadores de Performance</h2>
    
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
          <td style="text-align: center">R${self.faturamento_dia:.2f}</td>
          <td style="text-align: center">R${VerificarCores().meta_faturamento_dia:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_faturamentoDia(self.faturamento_dia)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Diversidade de Produto</td>
          <td style="text-align: center">{self.diversidade_produto_dia}</td>
          <td style="text-align: center">{VerificarCores().meta_diversidadeProduto_dia}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_diversidade_produtoDia(self.diversidade_produto_dia)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Ticket Médio</td>
          <td style="text-align: center">R${self.ticket_medio_dia:.2f}</td>
          <td style="text-align: center">R${VerificarCores().meta_ticketMedio_dia:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_ticketMedioDia(self.ticket_medio_dia)}">◙</font></td>
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
          <td style="text-align: center">R${self.faturamento_ano:.2f}</td>
          <td style="text-align: center">R${VerificarCores().meta_faturamento_ano:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_faturamentoAno(self.faturamento_ano)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Diversidade de Produto</td>
          <td style="text-align: center">{self.diversidade_produto_ano}</td>
          <td style="text-align: center">{VerificarCores().meta_diversidadeProduto_ano}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_diversidade_produtoAno(self.diversidade_produto_ano)}">◙</font></td>
        </tr>
        <tr>
          <td style="text-align: center">Ticket Médio</td>
          <td style="text-align: center">R${self.ticket_medio_ano:.2f}</td>
          <td style="text-align: center">R${VerificarCores().meta_ticketMedio_ano:.2f}</td>
          <td style="text-align: center"><font color="{VerificarCores().verificar_cor_ticketMedioAno(self.ticket_medio_ano)}">◙</font></td>
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


    def encaminhar_email_gerencia(self, emails_df, caminho_backup):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = emails_df.loc[emails_df['Loja'] == self.loja, 'E-mail'].values[0]
        mail.Subject = f'OnePage Day {self.dia_indicador.day}/{self.dia_indicador.month} - Loja {self.loja}'
        mail.HTMLBody = self.criar_email_gerencia()
        attachment = rf'{caminho_backup}\{self.loja}\{self.dia_indicador.month}_{self.dia_indicador.day}_{self.loja}.xlsx'
        mail.Attachments.Add(attachment)
        mail.Send()


    def criar_email_diretoria(self, ranking_faturamento_lojasDia, ranking_faturamento_lojasAno):
        email_text=f'''
        Bom dia,
        Segue em anexo o ranking do faturamento anual e Diário de todas as lojas.
        
        Melhor loja do dia {ranking_faturamento_lojasDia.index[0]} - Faturamento: R${ranking_faturamento_lojasDia.iloc[0,0]:.2f}
        Pior loja do dia {ranking_faturamento_lojasDia.index[-1]} - Faturamento: R${ranking_faturamento_lojasDia.iloc[-1,-1]:.2f}
        
        Melhor loja do ano {ranking_faturamento_lojasAno.index[0]} - Faturamento: R${ranking_faturamento_lojasAno.iloc[0,0]:.2f}
        Pior loja do ano {ranking_faturamento_lojasAno.index[-1]} - Faturamento: R${ranking_faturamento_lojasAno.iloc[-1,-1]:.2f}
        
        Qualquer dúvida, estou a disposição.
        Att. Renan D. Leal
        '''
        return email_text


    def encaminhar_email_diretoria(self, emails_df, email_diretoria,  caminho_ranking_dia, caminho_ranking_ano):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = emails_df.loc[emails_df['Loja'] == 'Diretoria', 'E-mail'].values[0]
        mail.Subject = f'Ranking diário e Anual ({self.dia_indicador.month}/{self.dia_indicador.day}).'
        mail.Body = email_diretoria
        attachment = caminho_ranking_dia
        mail.Attachments.Add(attachment)
        attachment = caminho_ranking_ano
        mail.Attachments.Add(attachment)
        mail.Send()