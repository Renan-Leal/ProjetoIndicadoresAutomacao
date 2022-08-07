<h1 align="center">Automação de Indicadores</h1>
<p><h2>Objetivo:</h2> Utilizando Python, o objetivo foi criar um processo da forma mais automática possível para calcular o OnePage de cada loja e enviar um email formatado em HTML exibindo os indicadores calculados para cada gerente. O arquivo completo com os dados da loja também é anexado.
Ao final da rotina, um e-mail com o ranking do faturamento anual e diário é encaminhado para a diretoria.</p>
<p></p>
<h2>Descrição:</h2>
<table width="200px" border="1">
  <tr><td>
<p style="text-align: justify;">Há uma grande rede de lojas de roupa com 25 lojas espalhadas por todo o Brasil. Todo dia, pela manhã, a equipe de análise de dados calcula os chamados One Pages e envia para o gerente de cada loja o OnePage da sua loja, bem como todas as informações usadas no cálculo dos indicadores.</p> 
<p style="text-align: justify;">Um One Page é um resumo muito simples e direto ao ponto, usado pela equipe de gerência de loja para saber os principais indicadores de cada loja e permitir em 1 página tanto a comparação entre diferentes lojas, quanto quais indicadores aquela loja conseguiu cumprir naquele dia ou não.</p>
<p style="text-align: justify;">Ao final da rotina, também deve encaminhar um e-mail para a diretoria com 2 rankings das lojas em anexo, 1 ranking do dia e outro ranking anual.Além disso, no corpo do e-mail, deve ressaltar qual foi a melhor e a pior loja do dia e também a melhor e pior loja do ano.</p> 
O processo organizará uma pasta de Backup para todas as lojas alocando cada loja em sua respectiva pasta.
  </td></tr>
</table>

<h2>Bibliotecas Utilizadas</h2>
<ul>
<li>Pandas - Para tratamento de dados e cálculo dos indicadores.</li>
<li>Pathlib - Para organização das pastas para backup.</li>
<li>Pywin32 - Para conexão com outlook.</li>
</ul>



