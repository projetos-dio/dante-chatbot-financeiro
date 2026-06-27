###################### IMPORTACAO BIBLIOTECAS ######################
import pandas as pd
import json
#import requests
import streamlit as st
from ollama import chat


MODEL = "gpt-oss:20b"


###################### CARREGAR DADOS ######################
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

###################### SYSTENM PROMPT ######################
SYSTEM_PROMPT = '''Você é o Dante, um assistente pessoal de finanças

OBJETIVO: 
Agir como um educador financeiro, baseando suas as respostas nas informações de perfil do cliente, sem nunca criticar investimentos, apresentando sempre fatos embasados

REGRAS:
1. Responda sempre baseadas em dados fornecidos como contexto
2. Não recomende nenhum tipo de investimentos, apenas instrui
3. Admita quando não souber de algo
4. Informe ao cliente, de forma direta, quando uma pergunta estiver fora do contexto que o agente é capaz de resopnder
5. Procure sempre usar linguagem simples e direta, caso o "perfil de investidor" do cliente seja "moderado" ou "agressivo", caso seja pertinente, poderá usar alguns termos mais técnicos, mas sempre lembrando que o cliente não é um especialista em finanças
6. Procure sempre fornecer respostas de um paragrafo. Caso seja necessário passar mais informações, evite se alongar mais de três paragrafos
...
'''


###################### CONTEXTO DO CLIENTE ######################
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}


TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}


ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}


PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
\n"""


###################### VARIAVEL PARA USO NO PROMPT ######################




###################### INICIALIZAÇÃO ASSISTENTE DE IA (DANTE) ######################
st.title("💵 Dante")
st.subheader("Assistente pessoal de finanças")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle user input
if pergunta := st.chat_input("Sua dúvida sobre finanças ..."):
    st.chat_message("user").write(pergunta)
    st.session_state.messages.append({"role": "user", "content": pergunta})
    GERAL = SYSTEM_PROMPT + contexto + pergunta 

    with st.spinner("Processando ..."):
        # Call Ollama for response
        response = chat(
            model=MODEL,
            #messages=st.session_state.messages,
            messages=[
                {'role': 'system', 'content': GERAL}
                #{'role': 'system', 'content': contexto}
                ],
            stream=False
        )
    
    assistant_msg = response["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
    st.chat_message("assistant").write(assistant_msg)