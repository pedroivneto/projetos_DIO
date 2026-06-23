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

## **FASE #1**
### **#001** 
* **Input**: Como fazer para guardar dinheiro?
* **Output**: <a ref="miniguia-finEdu-NotebookLM/respostas_arquivos/resposta#1.md">Resposta #1</a>
