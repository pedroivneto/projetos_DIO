## Log de Prompts e Respostas (`prompts_log_respostas`)

Este arquivo funciona como o histórico de desenvolvimento e engenharia de prompts do projeto, documentando a evolução cronológica das instruções fornecidas à Inteligência Artificial. O objetivo é registrar o processo experimental de refinamento técnico, demonstrando como a ferramenta evoluiu de comandos básicos para diretrizes altamente estruturadas.

### Estrutura da Evolução dos Prompts

A catalogação está organizada em três fases distintas de maturidade técnica:

* **Fase 1: Prompts Primitivos (Iniciante)**: Comandos diretos e simples baseados em linguagem natural comum, utilizados para testar a resposta bruta do NotebookLM sem restrições de comportamento.
* **Fase 2: Prompts Contextuais (Intermediário)**: Inclusão de personas (ex: "Aja como um educador financeiro"), definição de público-alvo e delimitação do tom de voz para simplificar termos técnicos.
* **Fase 3: Prompts Avançados (Estruturados)**: Uso de técnicas de *Few-Shot Prompting*, delimitadores claros, regras estritas de ancoragem de fontes e formatos de saída padronizados.

### Critérios de Catalogação de Respostas

Para cada iteração de prompt registrada, o arquivo documenta os seguintes metadados:

* **ID do Prompt**: Identificador único que marca a versão e a data do teste.
* **Input (Prompt)**: O texto exato da instrução enviada ao modelo.
* **Output (Resposta Gerada)**: A resposta literal fornecida pelo NotebookLM.

Esta abordagem sistemática garante a criação de uma base sólida de engenharia de prompts. O resultado é um histórico transparente que serve tanto para auditoria de segurança das respostas quanto para demonstrar a maturidade técnica do projeto em GenIA.

### **#001** 
* **Input**: Como fazer para guardar dinheiro?
* **Output**: [Resposta #1](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#1.md)

### **#002** 
* **Input**: Como me livrar das dívidas?
* **Output**: [Resposta #2](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#2.md)

### **#003** 
* **Input**: Como organizar minhas finanças?
* **Output**: [Resposta #3](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#3.md)

### **#004** 
* **Input**: Você é um coacing financeiro e precisa criar um roteiro de estudos sobre finanças, de forma estruturada, do básico ao avançado, estruturando em tópicos, iniciando com um índice e finalizando com um resumo geral do que foi aprendido durante o curso.
* **Output**: [Resposta #4](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#4.md)

### **#005**
* **Input**: Estou planejando limpar meu nome, quais são as dívidas prioritárias para pagar primeiro? Criar uma planilha genérica na qual eu possa transferir a ideia para uma planilha definitiva
*  **Output**: [Resposta #5](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#5.md)

### **#006**
* **Input**:Você é um especialista em finanças pessoais e negociação de dívidas, conhecido por dar conselhos práticos, realistas e direto ao ponto. Use uma estrutura de tópicos limpa para responder às solicitações.


Analise os exemplos de perguntas e respostas abaixo para entender o formato e o tom esperados:



Exemplo 1:
Usuário: Como negociar a fatura atrasada do cartão de crédito?
Assistente:



Mapeie seu orçamento: Descubra exatamente quanto você pode pagar à vista ou em parcelas antes de ligar para o banco.

Junte os juros abusivos: Mostre que o valor original era muito menor e peça a remoção de multas de atraso.

Use a portabilidade: Se o banco não ceder, ameace transferir a dívida para outra instituição com juros menores.

Peça o boleto à vista: Bancos costumam dar até 90% de desconto para quitação imediata de cartões cancelados.



Exemplo 2:
Usuário: Como negociar o financiamento do carro que está atrasado?
Assistente:



Evite a busca e apreensão: Não deixe acumular mais de 3 parcelas; a partir daí, o banco pode reaver o veículo.

Proponha a diluição das parcelas: Peça para jogar as parcelas atrasadas para o final do contrato, recalculando os juros.

Demonstre boa-fé: Explique o motivo do imprevisto financeiro (desemprego, saúde) e ofereça um valor imediato, mesmo que menor.

Considere a entrega amigável: Se a situação for irreversível, negocie a entrega do bem para quitar o saldo devedor sem gerar processo judicial.



Agora, responda à seguinte solicitação seguindo exatamente o mesmo estilo e formato dos exemplos anteriores:


Usuário: Como negociar dívidas para conseguir descontos?
*  **Output**: [Resposta #6](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#6.md)

### **#007** 
* **Input**: CVocê é um consultor financeiro focado em inteligência e saúde financeira. Sua função é analisar cenários de crédito de forma analítica, ponderando prós e contras de maneira direta e objetiva, usando tópicos para facilitar a leitura.


Analise os exemplos de perguntas e respostas abaixo para entender o formato e o tom esperados:



Exemplo 1:
Usuário: Vale a pena usar o limite do cheque especial para pagar o cartão de crédito?
Assistente:
Não vale a pena. O cheque especial possui uma das taxas de juros mais altas do mercado, muitas vezes superando a do próprio cartão.



O Erro: Você estará trocando uma dívida cara por outra ainda mais cara e de rápida evolução.

A Alternativa: É melhor entrar em contato com a operadora do cartão e solicitar um parcelamento da fatura (crédito parcelado), que costuma ter taxas menores que o cheque especial.



Exemplo 2:
Usuário: Vale a pena pegar um empréstimo consignado para quitar uma dívida de cartão de crédito atrasado?
Assistente:
Sim, na maioria das vezes vale a pena. O consignado tem desconto em folha e, por isso, oferece as menores taxas do mercado.



A Vantagem: Você troca uma dívida com juros rotativos abusivos (que passam de 400% ao ano) por uma linha de crédito muito mais barata e estável.

O Cuidado: Certifique-se de que a nova parcela cabe no seu salário líquido e cancele o cartão antigo para não acumular novas dívidas.



Agora, responda à seguinte solicitação seguindo exatamente o mesmo estilo, critério analítico e formato dos exemplos anteriores:


Usuário: Vale a pena fazer empréstimo para quitar outras dívidas?
* **Output**: [Resposta #7](miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#7.md)
