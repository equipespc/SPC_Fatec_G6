![alt text](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana1/logoFINAL.jpg)

## Projeto Integrador - 2° Semestre - ADS - B

  Projeto integrador proposto pela Faculdade de Tecnologia de São José dos Campos em parceria com a SPC Brasil, parceiro educacional, para os alunos dos 2° semestre do curso de  Análise e Desenvolvimento de Sistemas, tendo por finalidade o desenvolvimento de um produto que visa criar um benefício (agregar valor) em resolver uma demanda do parceiro educacional com base nos dados fornecidos mediante legislação do Cadastro Positivo.
  
  <p align="center">
  <img src="https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana1/Cad_Pos.jpg">
</p>

## **Integrantes**

  - [Marcos Yan Miranda Ferreira](https://github.com/equipespc) - **Scrum Master (SM)**.
  
    LinkedIn: [Marcos Yan](https://www.linkedin.com/in/yanmiranda/).

  - [Renan Vitor Fernandes Mendonça](https://github.com/RenanVitor) - **Product Owner (PO)**.
  
    LinkedIn: [Renan Vitor](https://www.linkedin.com/in/renan-vitor-a93814109/).

  - [Ana Clara Graciano](https://github.com/anaclaragraciano) - **Development Team (DT)**.
  
    LinkedIn: [Ana Clara](https://www.linkedin.com/in/ana-clara-graciano-41b5b9175/).

  - [João Pedro Apse Paes](https://github.com/JoaoPedroPaes) - **Development Team (DT)**.
  
    LinkedIn: [João Pedro](https://www.linkedin.com/in/joão-pedro-apse-paes-5339b51b2).

  - [Thiago Fernandes Canonici](https://github.com/thiagoCan) - **Development Team (DT)**.
  
    LinkedIn: [Thiago Fernandes](https://www.linkedin.com/in/thiago-canonici-943b97b8/).

## **Disciplinas**
  
  **- Sistemas de Informação** - Prof. Cláudio Etelvino de Lima.
  
  **- Engenharia de Software I** - Prof.ª Juliana Forin Pasquini Martinez.
  
  **- Linguagem de Programação** - Prof. Reinaldo Gen Ichiro Arakaki.


## **CPF Data Verifier: Conceito e Objetivo**

  <p align="center">
  <img width="400" height="300" src="https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/CPF_Data_Verifier_logo.png">
</p>

  A partir das remessas de dados de pessoas físicas oriundos das fontes (instituições financeiras), surgiu a ideia de criar o CPF Data Verfier (Verificador de Dados de CPF) que surge como solução para a área de crédito, no sentido de executar o alinhamento para o trabalho em frentes de Data Science e Data Preparation, permitindo ao analista de crédito não somente validar os CPFs das pessoas físicas repassadas como também relacionar informações que possibilitem o levantamento de perfis de consumidor (quanto ao potencial, ou não, de bom pagador, região de moradia no país, quantidades de parcelas e valores totais gastos) com base na síntese de gráficos e tabelas apresentados na tela da aplicação desktop.
  
   Dessa forma, fica facilitado para o analista de crédito o processo de identificar potenciais consumidores com bom histórico de pagamento e ter acesso também aos valores médios de gasto de consumo para definir estratégias e produtos alinhados com a realidade financeira de cada consumidor.
  
   A aplicação ainda conta com o indicador de erros encontrados durante a análise da remessa de dados das tabelas .csv para posterior envio para correção junto das fontes remetentes.
  
  Data Preparation consiste no processo de análise de dados em que são selecionadas as informações mais relevantes e potencialmente benéficas para a finalidade desejada pelo cliente. Tudo isso, na questão desse projeto, fica alinhado com o Data Science, que consiste na prática de extrair conhecimento, focado em tomada de decisão por meio de uma base de dados, independentemente se for em Big Data ou em um banco de dados tradicional. Sendo assim, há a presença do CPF Data Verifier, que é o responsável pela extração de dados e fornecer os insights para que a área de crédito da empresa possa fazer escolhas mais estratégicas com relação às pessoas físicas.
  
  <p align="center">
  <img width="600" height="200" src="https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana1/Data_Science.jpg">
</p>

  <p align="center">
  <img width="600" height="200" src="https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/Benef%C3%ADcios_Data_Science_e_Preparation.png">
</p>
  
 ## **Ferramentas e Tecnologias** ##
 
  As análises das tabelas de remessa de dados de Pessoas Físicas bem como a geração de gráficos e tabelas resultado, foram codificadas e realizadas utilizando-se o Jupyter Notebook, a biblioteca Matplotlib.pyplot (uso exclusivo para construção de gráficos) e o uso do PANDAS (Python) para a adaptação do código de validação do CPF fornecido, em JavaScript, pelo website da Receira Federal.
  
  As telas da interface da aplicação foram idealizadas com tecnologia de Bootstrap, CSS, Html e JavaScript, contando ainda com o código da análise para a execução e exibição da mesma no próprio front-end.
  
  Os dados analisados são referentes à [2ª Remessa de dados](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana%206/Dados%20-%202%C2%AA%20Remessa).

## **Funcionamento e embasamento técnico** ##
  
  A aplicação, desenvolvida incialmente para Desktops, com foco em pessoa física para o setor de crédito do SPC Brasil, visa, por meio de algoritmo próprio fornecido pela receita federal (dando grau de realidade para a solução), validar os CPFs repassados na remessa de dados das mais diversas instituições financeiras a fim de cruzar os dados destes correspondentes ao histórico de consumo junto à fonte remetente e levantar informações a serem exibidas nas telas da solução.
  
  As análises permitiram concluir um espaço amostral, da 2ª remessa em questão, de 12 CPFs validados com suas respectivas regiões e particularidades de crédito, como exemplo de resultado de análise. Abaixo é possível visualizar dois gráficos desse espaço amostral separado por região do país em termos de origem e moradia atual.
  
 **Exemplo: CPFs por Estado de Origem e Estado de Moradia Atual**
 ![alt text](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/Gr%C3%A1fico_CPF%20Estado_e_Origem.PNG)
 
 **Exemplo: Rodando a aplicação**
 
 **OBS.: O vídeo de funcionamento da aplicação pode ser baixado para visualização [Clicando Aqui](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/Gif%20da%20Aplica%C3%A7%C3%A3o/VID-20200712-WA0020.mp4).**
 
 ![Rodando o CPF Data Verifier](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/Gif%20da%20Aplica%C3%A7%C3%A3o/Spc_gif.gif)
 
 ## **Vídeo de apresentação do Produto** ##
 
 O vídeo de apresentação do CPF Data Verifier pode ser visualizado no YouTube [Clicando aqui](https://youtu.be/ysEeVj3-Prs).
 
## **Diagrama da solução** ##
 
 <p align="center">
  <img width="500" height="400" src="https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/DCU_PI_SPRINT6.png">
</p>

## **Entregas** ##

  Foi definido, em calendário próprio fornecido pela FATEC, que o projeto de desenvolvimento deveria ser feito em um total de seis entregas realizadas ao longo do semestre dentro dos prazos que se observa a seguir:
  
  - [Entrega 1](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana1) - 16/03/2020 à 20/03/2020;
  
  - [Entrega 2](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana2) - 11/05/2020 à 15/05/2020;
  
  - [Entrega 3](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana3) - 25/05/2020 à 29/06/2020;
  
  - [Entrega 4](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana%204) - 08/06/2020 à 12/06/2020;
  
  - [Entrega 5](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana%205) - 22/06/2020 à 26/06/2020;
  
  - [Entrega 6](https://github.com/equipespc/SPC_Fatec_G6/tree/master/Semana%206) - 06/07/2020 à 12/06/2020;
  
  ## **Backlog das entregas** ##
  
  - [Backlog da Entrega 1](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana1/Documenta%C3%A7%C3%A3o/PI_Modelo_VISAO_DESENV_OO.pdf)
  
  - [Backlog da Entrega 2](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana2/Documenta%C3%A7%C3%A3o/Sprint2_time6%20(2).pdf)
  
  - [Backlog da Entrega 3](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana3/Documentos/Product_Backlog_Grupo%206.xlsx)
  
  - [Backlog da Entrega 4](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%204/Back-end/Product_Backlog_Grupo%206_novo.xlsx)
  
  - [Backlog da Entrega 5](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%205/Product_Backlog_Grupo%206%20(2).xlsx)
  
  - [Backlog da Entrega 6](https://github.com/equipespc/SPC_Fatec_G6/blob/master/Semana%206/Product_Backlog_Grupo%206_novo.xlsx)






