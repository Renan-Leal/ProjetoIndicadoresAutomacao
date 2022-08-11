<h1 style="text-align: center">Explicação API:</h1>

<p>Para o time da empresa, cria-se uma API para consumo dos indicadores.</p>

<p>A API disponibiliza os dados seguinte maneira:</p> 
<p>"Nome Loja": [Faturamento Diário, Faturamento Anual, Ticket Médio Diário, Ticket Médio Anual, Diversidade de Produto Diária, Diversidade de Produto Anual].</p> 

O usuário poderá navegar pelas seguintes URL:

<p>/indicadores/lojas - Exibe todas as lojas com todos os indicadores(Faturamento Diário, Faturamento Anual, Ticket Médio Diário, Ticket Médio Anual, Diversidade de Produto Diária, Diversidade de Produto Anual).</p>

<p>/indicadores/lojas/faturamento/diario - Exibe as lojas e o Faturamento Diário de cada uma.</p>

<p>/indicadores/lojas/faturamento/anual -  Exibe as lojas e o Faturamento Anual de cada uma.</p>

<p>/indicadores/lojas/ticketMedio/diario -  Exibe as lojas e o Ticket Médio Diário de cada uma.</p>

<p>/indicadores/lojas/ticketMedio/anual -  Exibe as lojas e o Ticket Médio Anual de cada uma.</p>

<p>/indicadores/lojas/diversidadeProduto/diario - Exibe as lojas e a Diversidade de Produto Diário de cada uma.</p>

<p>/indicadores/lojas/diversidadeProduto/anual - Exibe as lojas e a Diversidade de Produto Anual de cada uma.</p>

<p>/indicadores/lojas/<Pesquisar Loja> -  Exibe a loja pesquisada e todos os seus indicadores.
Exemplo: /indicadores/lojas/Iguatemi Esplanada</p>


<p>/indicadores/lojas/faturamento/total - Exibe o Faturamento Total da empresa, ou seja, soma do Faturamento Anual de todas as lojas.</p>
