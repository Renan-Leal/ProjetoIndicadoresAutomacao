<h1 style="text-align: center">Objetivo:</h1>

<p>Criar uma API para consumo dos indicadores calculados de cada loja.</p>

<h2>Como a API disponibiliza os dados:</h2> 
<p>"Nome Loja": [Faturamento Diário, Faturamento Anual, Ticket Médio Diário, Ticket Médio Anual, Diversidade de Produto Diária, Diversidade de Produto Anual].</p> 

<h3>O usuário poderá navegar pelas seguintes URL:</h3>

<ul>
  <li><p><b><u>/indicadores/lojas</u></b> - Exibe todas as lojas com todos os indicadores(Faturamento Diário, Faturamento Anual, Ticket Médio Diário, Ticket Médio Anual, Diversidade de Produto Diária, Diversidade de Produto Anual).</p></li>

  <li><p><b>indicadores/lojas/faturamento/diario/</b> - Exibe as lojas e o Faturamento Diário de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/faturamento/anual</b> -  Exibe as lojas e o Faturamento Anual de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/ticketMedio/diario</b> -  Exibe as lojas e o Ticket Médio Diário de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/ticketMedio/anual</b> -  Exibe as lojas e o Ticket Médio Anual de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/diversidadeProduto/diario</b> - Exibe as lojas e a Diversidade de Produto Diário de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/diversidadeProduto/anual</b> - Exibe as lojas e a Diversidade de Produto Anual de cada uma.</p></li>

  <li><p><b>/indicadores/lojas/<Pesquisar Loja></b> -  Exibe a loja pesquisada e todos os seus indicadores.<p>
  <b>Exemplo:</b> /indicadores/lojas/Iguatemi Esplanada</p></li>


  <li><p><b>/indicadores/lojas/faturamento/total</b> - Exibe o Faturamento Total da empresa, ou seja, soma do Faturamento Anual de todas as lojas.</p></li>
