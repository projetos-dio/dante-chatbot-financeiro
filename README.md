# 💵 Dante - Assistente pessoal de finanças

## Contexto

Em 2025 uma pesquisa realizada pelo Observatório Febraban apontou que 55% dos brasileiros entende pouco ou nada sobre educação financeira, e reconhecem a importância deste tema.
Esta mesma pesquisa informa que 75% das pessoas afirma ter algum nível de acompanhamento ou controle das suas finanças pessoais.
Esses foram os motivadores para a criação do Dante, o assistente pessoal focado em finanças.


- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Simplifica o entendimento das finanças pessoais e esclarece sobre possibilidades de investimentos, sempre levando em consideração o perfil de investidor do cliente.
- **Persona e Tom de Voz:** Age como um educador, baseia as respostas nas informações de perfil do cliente. Sempre responde em tom cordial e informal
- **Arquitetura:** Presente no documento [`01-documentacao-agente.md`](https://github.com/projetos-dio/dante-chatbot-financeiro/edit/main/docs/01-documentacao-agente.md)
- **Segurança:** Para evitar imprecisões e alucinações baseia todas as respostas em uma base robusta de conhecimento e nas informações do perfil do usuário

---

### 2. Base de Conhecimento

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

---

### 3. Prompts do Agente

- **System Prompt, Exemplos de Interação e Tratamento de Edge Cases:** [03-prompts.md](https://github.com/projetos-dio/dante-chatbot-financeiro/blob/main/docs/03-prompts.md) utilizados na solução

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo: Streamlit
- Integração com LLM: Base local do [gpt-oss:20b](https://ollama.com/library/gpt-oss:20b)
- Base de conhecimento: Local, presente na [`📁data/`](./data/)


---

### 5. Avaliação e Métricas

O padrão de avaliação utilizado para esta aplicação foram os testes estruturados. O assistente teve êxito em todos os testes realizados de acordo com as métricas sugeridas.

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

---

## Ferramentas Utilizadas na Criação da Solução

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **Editor de código** | [Vistual Studio](https://code.visualstudio.com/) |
| **Desenvolvimento** | [Python](https://www.python.org/), [Streamlit](https://streamlit.io/), [Ollama](https://ollama.ai/) |
| **LLMs** | [GPT OSS](https://ollama.com/library/gpt-oss:20b) |

---

## Estrutura do Repositório
```
# 📁 dante-chatbot-financeiro/
│
├── 📁 assets/							# Imagens e diagramas
│   └── Sucesso01.png
│
├── 📁 data/							# Dados mockados para o agente
│   ├── historico_atendimento.csv		# Histórico de atendimentos (CSV
│   ├── perfil_investidor.json			# Perfil do cliente (JSON
│   ├── produtos_financeiros.json		# Produtos disponíveis (JSON)
│   └── transacoes.csv					# Histórico de transações (CSV)
│
├── 📁 docs/							# Documentação do projeto
│   ├── 01-documentacao-agente.md		# Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md			# Estratégia de dados
│   ├── 03-prompts.md					# Engenharia de prompts
│   ├── 04-metricas.md					# Avaliação e métricas
│   └── 05-pitch.md						# Pitch do projeto
│
├── 📁 src/								# Código da aplicação
│   ├── dante-assistente-ia-1.4.py		# Código fonte (Python) da solução
│   └── requirements.txt				# Requisitos de software
│
└── 📄 README.md
```
---
