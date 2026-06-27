# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

- O carregamento dos estava traznedo caracteres mal formatados, inserido o padrão de formatação `encoding='utf-8'` para solução do problema

---

## Estratégia de Integração

### Como os dados são carregados?
``` python

###################### IMPORTACAO BIBLIOTECAS ######################
import pandas as pd
import json

###################### CARREGAR DADOS ######################
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

```

### Como os dados são usados no prompt?
Os arquivos presentes dentro da pasta `data` são inseridos no código dinamicamente. A cada promnpt eles são fornecidos como base, antes do texto de interação do usuário.
A inserção dos dados acontece dentro do chat do streamlit

```python
response = chat(
            model=MODEL,
            #messages=st.session_state.messages,
            messages=[
                {'role': 'system', 'content': GERAL}
                #{'role': 'system', 'content': contexto}
                ],
            stream=False
        )
```


---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Fulano de Tal
- Perfil: Moderado
- Reserva: R$ 5.000

Últimas transações:
- 01/10: Aluguel   - R$ 1200
- 02/10: Mercado   - R$ 450
- 03/10: Streaming - R$ 55
...
```
