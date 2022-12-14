<h1 align="center">Automação de Indicadores</h1>
<p><h2>Objetivo:</h2> Utilizando Python, o objetivo foi criar um processo da forma mais automática possível para calcular o OnePage de cada loja e enviar um email formatado em HTML exibindo os indicadores calculados para cada gerente. O arquivo completo com os dados da loja também é anexado.
Ao final da rotina, um e-mail com o ranking do faturamento anual e diário é encaminhado para a diretoria.</p>
<p></p>
<hr>
<h2>Contexto:</h2>
<table width="200px" border="1">
  <tr><td>
    <p style="text-align: justify;">Há uma grande rede de lojas de roupa com 25 lojas espalhadas por todo o Brasil. Todo dia, pela manhã, a equipe de análise de dados calcula os chamados One Pages e envia para o gerente de cada loja o OnePage da sua loja, bem como a base de dados detalhada usada no cálculo dos indicadores.</p> 
    <p style="text-align: justify;">Um One Page é um resumo muito simples e direto ao ponto, usado pela equipe de gerência de loja para saber os principais indicadores de cada loja e permitir em 1 página tanto a comparação entre diferentes lojas, quanto quais indicadores aquela loja conseguiu cumprir naquele dia ou não.</p>
    <p style="text-align: justify;">Ao final da rotina, a equipe também deve encaminhar um e-mail para a diretoria com 2 rankings das lojas em anexo, 1 ranking do dia e outro ranking anual.Além disso, no corpo do e-mail, deve ressaltar qual foi a melhor e a pior loja do dia e também a melhor e pior loja do ano.</p> 
    O processo organizará uma pasta de Backup para todas as lojas alocando cada arquivo excel da loja em sua respectiva pasta. No escopo do projeto, a pasta gerada pela automação está disposta na primeira página com o nome de Backup Arquivos Lojas.</p>
    <p style="text-align: justify;">Para o time de dados, é gerado uma API para consumo dos indicadores da empresa. A explicação da mesma está disposta no ReadMe da pasta Projeto.</p>
   <p style="text-align: justify;">Para facilitar essa Rotina, a equipe decidiu criar uma aplicação que automatize esse processo inteiro e rode em minutos otimizando o tempo e aumentando a produtividade do setor.</p>
  </td></tr>
</table>
<hr>
<h2>Bibliotecas Utilizadas</h2>
<ul>
  <li><b>Pandas</b> - Para tratamento de dados e cálculo dos indicadores.</li>
  <li><b>Pathlib</b> - Para organização das pastas para backup.</li>
  <li><b>Pywin32</b> - Para conexão com outlook.</li>
  <li><b>Flask</b> - Para criação da API de consumo dos indicadores.</li>
</ul>
<hr>
<h2>Como rodar no seu computador:</h2>
<ul>
  <li><b>Passo 1</b> - Instale e importe as bibliotecas listadas acima.</li>
  <li><b>Passo 2</b> - Faça o Download das bases de dados que estão na pasta Base de Dados.</li>
  <li><b>Passo 3</b> - Altere os caminhos que estão nas variáveis <b>caminho_baseDados</b> e <b>caminho_backup</b> adaptando para os caminhos do seu computador. Para auxiliar nesse processo, as variáveis estarão sinalizadas com um comentário escrito <b>Me altere!!!</b> ao lado direito. Ambas variáveis podem ser encontradas no <b>início</b> do <b>arquivo Main</b>.</li>
  <li><b>Passo 4</b> - Garanta que você já autenticou no outlook do seu computador ao menos uma vez.</li>
  <li><b>Passo 5</b> - Altere os <b>time.sleep()</b> conforme a capacidade de processamento do seu computador.</li>
  <li><b>Passo 6</b> - Be Happy!</li>
</ul>




