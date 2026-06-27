# Avaliação e Métricas

## Como Avaliar seu Agente

O padrão de avaliação utilizado para esta aplicação foram os **testes estruturados**.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |


---

## Cenários de Teste

### Teste 1: Validação do carregamento das informações de prompt
- **Pergunta:** "Oi, quem é você?"
- **Resposta esperada:** Informações condizentes com o perfil de agente definido nas configurações`
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Teste da capacidade de processamento dos arquivos de contexto do usuário
- **Pergunta:** "Com o que mais gastei ultimamente?"
- **Resposta esperada:** Somatória dos gastos mais elevados presentes na base separados por categoria
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo para hoje?"
- **Resposta esperada:** Agente informa que só possui informações sobre assunstos relacionados a finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende R$ 1000 investidos na ação BBAS3?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- Todas as interações com o agente foram bem sucedidas até o momento

**O que pode melhorar:**
- Melhorar a formatação de saída do agente para que represente cifras monetárias mais adequdamente

