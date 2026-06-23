# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Simplificar o entendimento das finanças pessoais e esclarecer sobre possibilidades de investimentos.


### Solução
> Como o agente resolve esse problema de forma proativa?

Esclarecendo conceitos com informações baseadas no perfil de cada cliente. Considera o perfil de investimentos de cada cliente para dosar como cada informação será passada, trazendo uma experiência extremamente personalizada.
Apesar de não sugerir investimentos o agente é capaz de fazer comparções entre investimentos e informar pontos chave para que cada cliente possa tomar suas próprias decisões de forma mais embasada.

### Público-Alvo
> Quem vai usar esse agente?

Todos os clientes que desejem informações sobre investimentos ou que busquem aprender sobre os diversos tipos de produtos financeiros oferecidos pelo banco.

---|###---###---###--->

## Persona e Tom de Voz

### Nome do Agente
[Nome escolhido]

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

[Sua descrição aqui]

### Tom de Comunicação
> Formal, informal, técnico, acessível?

[Sua descrição aqui]

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
